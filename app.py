from flask import Flask, render_template, request, send_file
import os
import csv
from werkzeug.utils import secure_filename

from utils.pdf_parser import extract_text_from_pdf
from utils.text_processor import preprocess_text
from utils.ranker import calculate_ranking


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# --------------------------------------------------
# Allowed File Types
# --------------------------------------------------

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# --------------------------------------------------
# Resume Ranking
# --------------------------------------------------

@app.route("/rank", methods=["POST"])
def rank_resumes():

    job_description = request.form.get(
        "job_description",
        ""
    ).strip()

    resume_files = request.files.getlist("resumes")

    # Validate job description
    if not job_description:
        return render_template(
            "index.html",
            error="Please enter a job description."
        )

    # Validate resumes
    if not resume_files or all(
        file.filename == ""
        for file in resume_files
    ):
        return render_template(
            "index.html",
            error="Please upload at least one resume."
        )

    # --------------------------------------------------
    # Process Job Description
    # --------------------------------------------------

    cleaned_job_description = preprocess_text(
        job_description
    )

    resumes = {}

    invalid_files = []

    # --------------------------------------------------
    # Process Uploaded Resumes
    # --------------------------------------------------

    for resume_file in resume_files:

        if resume_file.filename == "":
            continue

        # Check file type
        if not allowed_file(resume_file.filename):
            invalid_files.append(resume_file.filename)
            continue

        filename = secure_filename(
            resume_file.filename
        )

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        resume_file.save(file_path)

        # Extract text from PDF
        raw_text = extract_text_from_pdf(
            file_path
        )

        if not raw_text:
            continue

        # Clean text for TF-IDF
        cleaned_text = preprocess_text(
            raw_text
        )

        resumes[filename] = cleaned_text

    # --------------------------------------------------
    # Check Invalid Files
    # --------------------------------------------------

    if invalid_files and not resumes:
        return render_template(
            "index.html",
            error=(
                "Only PDF files are supported. "
                "Please upload PDF resumes."
            )
        )

    # --------------------------------------------------
    # Check Resume Extraction
    # --------------------------------------------------

    if not resumes:
        return render_template(
            "index.html",
            error=(
                "Could not extract text from "
                "the uploaded PDF resumes."
            )
        )

    # --------------------------------------------------
    # Calculate Rankings
    # --------------------------------------------------

    results = calculate_ranking(
        cleaned_job_description,
        resumes
    )

    # --------------------------------------------------
    # Generate CSV Report
    # --------------------------------------------------

    report_path = os.path.join(
        REPORT_FOLDER,
        "resume_ranking_report.csv"
    )

    with open(
        report_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Rank",
            "Candidate",
            "TF-IDF Score",
            "Skill Score",
            "Final Score",
            "Matched Skills",
            "Missing Skills"
        ])

        for result in results:

            writer.writerow([
                result["rank"],
                result["candidate"],
                result["similarity_score"],
                result["skill_score"],
                result["final_score"],
                ", ".join(
                    result["matched_skills"]
                ),
                ", ".join(
                    result["missing_skills"]
                )
            ])

    return render_template(
        "results.html",
        results=results
    )


# --------------------------------------------------
# Download CSV Report
# --------------------------------------------------

@app.route("/download-report")
def download_report():

    report_path = os.path.join(
        REPORT_FOLDER,
        "resume_ranking_report.csv"
    )

    if not os.path.exists(report_path):
        return "Report not available."

    return send_file(
        report_path,
        as_attachment=True,
        download_name="resume_ranking_report.csv"
    )


# --------------------------------------------------
# Run Flask Application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
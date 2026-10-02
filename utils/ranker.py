from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.skill_extractor import extract_skills, compare_skills


def calculate_ranking(job_description, resumes):
    """
    Rank resumes using:
    1. TF-IDF cosine similarity
    2. Skill matching

    Final Score:
        70% TF-IDF similarity
        30% Skill matching
    """

    if not job_description or not resumes:
        return []

    candidate_names = list(resumes.keys())
    resume_texts = list(resumes.values())

    # -------------------------------------------------
    # STEP 1: TF-IDF similarity
    # -------------------------------------------------

    documents = [job_description] + resume_texts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]

    similarity_scores = cosine_similarity(
        job_vector,
        resume_vectors
    )[0]

    # -------------------------------------------------
    # STEP 2: Extract required job skills
    # -------------------------------------------------

    job_skills = extract_skills(job_description)

    results = []

    # -------------------------------------------------
    # STEP 3: Analyze every resume
    # -------------------------------------------------

    for name, similarity, resume_text in zip(
        candidate_names,
        similarity_scores,
        resume_texts
    ):

        resume_skills = extract_skills(resume_text)

        skill_analysis = compare_skills(
            job_skills,
            resume_skills
        )

        # Convert similarity to percentage
        similarity_percentage = float(similarity) * 100

        skill_score = skill_analysis["skill_score"]

        # -------------------------------------------------
        # STEP 4: Calculate final score
        # -------------------------------------------------

        final_score = (
            similarity_percentage * 0.70
            + skill_score * 0.30
        )

        results.append({
            "candidate": name,
            "similarity_score": round(
                similarity_percentage, 2
            ),
            "skill_score": round(
                skill_score, 2
            ),
            "final_score": round(
                final_score, 2
            ),
            "matched_skills": skill_analysis[
                "matched_skills"
            ],
            "missing_skills": skill_analysis[
                "missing_skills"
            ]
        })

    # -------------------------------------------------
    # STEP 5: Sort candidates by final score
    # -------------------------------------------------

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    # -------------------------------------------------
    # STEP 6: Assign ranking numbers
    # -------------------------------------------------

    for rank, result in enumerate(results, start=1):
        result["rank"] = rank

    return results
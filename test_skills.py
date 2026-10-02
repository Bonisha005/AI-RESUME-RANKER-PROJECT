from utils.skill_extractor import extract_skills
from utils.skill_extractor import compare_skills


job_description = """
We are looking for a Python developer with experience
in Flask, REST API, SQL, Machine Learning, Git and Docker.
"""


resume_text = """
Software developer with experience in Python, Flask,
SQL, Machine Learning and Git.

Worked on REST API projects and web applications.
"""


# Extract skills
job_skills = extract_skills(job_description)
resume_skills = extract_skills(resume_text)


print("\n========== JOB SKILLS ==========")
print(job_skills)

print("\n========== RESUME SKILLS ==========")
print(resume_skills)


# Compare skills
result = compare_skills(
    job_skills,
    resume_skills
)


print("\n========== SKILL ANALYSIS ==========")

print("Matched Skills:")
print(result["matched_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])

print("\nSkill Match:")
print(f"{result['skill_score']}%")
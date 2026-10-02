from utils.ranker import calculate_ranking


job_description = """
We are looking for a Python Developer with experience
in Python, Flask, REST API, SQL, Machine Learning,
Git and Docker.
"""


resumes = {
    "Candidate_A": """
    Python Flask REST API SQL Machine Learning Git Docker
    AWS
    """,

    "Candidate_B": """
    Java Spring Boot Hibernate MySQL
    """,

    "Candidate_C": """
    Python Flask Machine Learning Git
    React MongoDB
    """
}


results = calculate_ranking(job_description, resumes)


print("\n======================================")
print("       AI RESUME RANKING RESULTS")
print("======================================\n")


for result in results:

    print(f"Rank: {result['rank']}")
    print(f"Candidate: {result['candidate']}")
    print(f"TF-IDF Score: {result['similarity_score']}%")
    print(f"Skill Score: {result['skill_score']}%")
    print(f"Final Score: {result['final_score']}%")

    print(
        f"Matched Skills: "
        f"{', '.join(result['matched_skills'])}"
    )

    print(
        f"Missing Skills: "
        f"{', '.join(result['missing_skills'])}"
    )

    print("--------------------------------------")
from utils.ranker import calculate_similarity


job_description = """
Python developer with experience in Flask,
REST API, SQL, Machine Learning and Git.
"""


resumes = {

    "Candidate_A": """
    Python Flask REST API SQL Machine Learning Git
    Docker AWS
    """,

    "Candidate_B": """
    Java Spring Boot Hibernate MySQL
    """,

    "Candidate_C": """
    Python Flask Machine Learning Git
    React MongoDB
    """
}


results = calculate_similarity(
    job_description,
    resumes
)


print("\n========== RANKING RESULTS ==========\n")

for result in results:

    print(
        f"Rank {result['rank']} | "
        f"{result['candidate']} | "
        f"{result['score']}%"
    )
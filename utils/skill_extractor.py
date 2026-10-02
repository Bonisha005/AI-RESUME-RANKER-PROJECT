import re


# Canonical skill name -> possible forms found in resumes/JDs
SKILL_ALIASES = {
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "C#": ["c#", "csharp"],
    "JavaScript": ["javascript"],
    "TypeScript": ["typescript"],
    "HTML": ["html"],
    "CSS": ["css"],

    "React": ["react", "react.js", "reactjs"],
    "Node.js": ["node.js", "nodejs"],
    "Express": ["express", "express.js", "expressjs"],
    "Flask": ["flask"],
    "Django": ["django"],
    "FastAPI": ["fastapi"],

    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql"],
    "MongoDB": ["mongodb"],

    "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"],
    "Artificial Intelligence": [
        "artificial intelligence",
        "ai"
    ],
    "Natural Language Processing": [
        "natural language processing",
        "nlp"
    ],

    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Scikit-learn": [
        "scikit-learn",
        "scikitlearn"
    ],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],

    "Git": ["git"],
    "GitHub": ["github"],
    "Docker": ["docker"],
    "AWS": ["aws"],
    "Azure": ["azure"],

    "REST API": [
        "rest api",
        "restapi"
    ],
    "REST": ["rest"],

    "Spring Boot": ["spring boot"],

    "Data Structures": ["data structures"],
    "Algorithms": ["algorithms"],
    "Object-Oriented Programming": [
        "object oriented programming",
        "object-oriented programming",
        "oop"
    ]
}


def normalize_text(text):
    """
    Normalize text so different forms of the same
    technology can be matched.
    """

    if not text:
        return ""

    text = text.lower()

    replacements = {
        "react.js": "reactjs",
        "node.js": "nodejs",
        "next.js": "nextjs",
        "vue.js": "vuejs",
        "express.js": "expressjs",
        "c++": "cpp",
        "c#": "csharp",
        "scikit-learn": "scikitlearn",
        "rest api": "restapi",
        "object-oriented programming": "object oriented programming",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def contains_skill(text, skill_variants):
    """
    Check whether any version of a skill exists in the text.
    """

    for variant in skill_variants:

        variant = normalize_text(variant)

        # Escape special regex characters
        pattern = r"(?<!\w)" + re.escape(variant) + r"(?!\w)"

        if re.search(pattern, text):
            return True

    return False


def extract_skills(text):
    """
    Extract recognized technical skills from text.

    Returns canonical skill names.
    """

    if not text:
        return []

    normalized_text = normalize_text(text)

    found_skills = []

    for skill, variants in SKILL_ALIASES.items():

        if contains_skill(normalized_text, variants):
            found_skills.append(skill)

    return sorted(found_skills)


def compare_skills(job_skills, resume_skills):
    """
    Compare skills required by the job with skills
    found in the resume.
    """

    job_set = set(job_skills)
    resume_set = set(resume_skills)

    matched = sorted(job_set.intersection(resume_set))
    missing = sorted(job_set - resume_set)

    if job_set:
        skill_match_percentage = (
            len(matched) / len(job_set)
        ) * 100
    else:
        skill_match_percentage = 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_score": round(skill_match_percentage, 2)
    }
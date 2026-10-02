# AI Resume Ranker

An AI-powered resume screening and ranking system that analyzes resumes against a given job description using NLP, TF-IDF similarity, and skill matching.

## Features

- Upload multiple PDF resumes
- Extract text from PDF resumes
- Preprocess resume and job-description text
- Extract technical skills
- Calculate TF-IDF similarity
- Calculate skill-match percentage
- Generate a final candidate score
- Rank candidates automatically
- Display matched and missing skills
- Download ranking results as a CSV report
- PDF file validation
- Responsive web interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- NLTK
- PyPDF
- Pandas
- NumPy
- spaCy

## Project Architecture

```text
AI Resume Ranker
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── utils/
│   ├── __init__.py
│   ├── pdf_parser.py
│   ├── text_processor.py
│   ├── skill_extractor.py
│   └── ranker.py
│
├── uploads/
│
├── reports/
│
└── test files
    ├── test_parser.py
    ├── test_preprocessing.py
    ├── test_skills.py
    └── test_complete_ranker.py
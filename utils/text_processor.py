import re
import spacy


# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Preprocess resume or job-description text using SpaCy.

    Steps:
    1. Convert text to lowercase
    2. Remove URLs
    3. Normalize common technical terms
    4. Remove unwanted characters
    5. Tokenize using SpaCy
    6. Remove stopwords
    7. Remove very short tokens
    8. Lemmatize words using SpaCy
    """

    if not text:
        return ""

    # ---------------------------------------------
    # Convert text to lowercase
    # ---------------------------------------------

    text = text.lower()


    # ---------------------------------------------
    # Remove URLs
    # ---------------------------------------------

    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )


    # ---------------------------------------------
    # Normalize common technical terms
    # ---------------------------------------------

    replacements = {
        "react.js": "reactjs",
        "node.js": "nodejs",
        "next.js": "nextjs",
        "vue.js": "vuejs",
        "express.js": "expressjs",
        "c++": "cpp",
        "c#": "csharp",
        "scikit-learn": "scikitlearn",
        "rest api": "restapi"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)


    # ---------------------------------------------
    # Keep useful characters
    # ---------------------------------------------

    text = re.sub(
        r"[^a-zA-Z0-9+#.\s]",
        " ",
        text
    )


    # ---------------------------------------------
    # Remove extra spaces
    # ---------------------------------------------

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()


    # ---------------------------------------------
    # SpaCy tokenization and preprocessing
    # ---------------------------------------------

    doc = nlp(text)

    cleaned_words = []

    technical_tokens = {
        "reactjs",
        "nodejs",
        "nextjs",
        "vuejs",
        "expressjs",
        "cpp",
        "csharp",
        "scikitlearn",
        "restapi"
    }

    for token in doc:

        # Remove spaces and punctuation
        if token.is_space or token.is_punct:
            continue

        # Remove stopwords
        if token.is_stop:
            continue

        # Remove very short tokens
        if len(token.text) <= 1:
            continue

        # Keep technical tokens unchanged
        if token.text in technical_tokens:
            cleaned_words.append(token.text)

        else:
            # SpaCy lemmatization
            lemma = token.lemma_.strip()

            if lemma:
                cleaned_words.append(lemma)


    return " ".join(cleaned_words)
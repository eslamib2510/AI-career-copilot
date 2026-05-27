import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ==========================
# DOWNLOAD NLTK
# ==========================

nltk.download("stopwords")
nltk.download("wordnet")

# ==========================
# TOOLS
# ==========================

stop_words = set(
    stopwords.words("english")
)

lemmatizer = WordNetLemmatizer()

# ==========================
# CLEAN FUNCTION
# ==========================

def clean_text(text):

    # lowercase
    text = text.lower()

    # remove urls
    text = re.sub(
        r"http\S+",
        "",
        text
    )

    # remove emails
    text = re.sub(
        r"\S+@\S+",
        "",
        text
    )

    # remove numbers
    text = re.sub(
        r"\d+",
        "",
        text
    )

    # remove symbols
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # tokenize
    words = text.split()

    # remove stopwords
    words = [

        word for word in words

        if word not in stop_words
    ]

    # lemmatization
    words = [

        lemmatizer.lemmatize(word)

        for word in words
    ]

    return " ".join(words)
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.linear_model import (
    LogisticRegression
)

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from preprocessing import clean_text

# ====================================
# LOAD DATASET
# ====================================

df = pd.read_csv(
    "data/Resume.csv"
)

# ====================================
# REMOVE NULL VALUES
# ====================================

df = df.dropna()

# ====================================
# INPUTS AND LABELS
# ====================================

X = df["Resume_str"]

y = df["Category"]

# ====================================
# NLP PREPROCESSING
# ====================================

X = X.apply(clean_text)

# ====================================
# TF-IDF FEATURE ENGINEERING
# ====================================

vectorizer = TfidfVectorizer(

    stop_words="english",

    ngram_range=(1, 2),

    max_features=10000,

    min_df=2,

    max_df=0.9
)

X_vectorized = vectorizer.fit_transform(X)

# ====================================
# TRAIN TEST SPLIT
# ====================================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X_vectorized,
        y,
        test_size=0.2,
        random_state=42
    )
)

# ====================================
# HYPERPARAMETER TUNING
# ====================================

parameters = {

    "C": [0.1, 1, 10],

    "solver": [
        "liblinear",
        "lbfgs"
    ],

    "max_iter": [
        1000
    ]
}

grid_search = GridSearchCV(

    LogisticRegression(),

    parameters,

    cv=3,

    scoring="f1_weighted",

    verbose=1,

    n_jobs=-1
)

# ====================================
# TRAIN MODEL
# ====================================

grid_search.fit(
    X_train,
    y_train
)

# ====================================
# BEST MODEL
# ====================================

model = grid_search.best_estimator_

print(
    "\n===== BEST PARAMETERS =====\n"
)

print(
    grid_search.best_params_
)

# ====================================
# PREDICTIONS
# ====================================

predictions = model.predict(
    X_test
)

# ====================================
# EVALUATION METRICS
# ====================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "\n===== MODEL ACCURACY =====\n"
)

print(
    f"Accuracy: {accuracy:.2f}"
)

print(
    "\n===== CLASSIFICATION REPORT =====\n"
)

print(
    classification_report(
        y_test,
        predictions
    )
)

# ====================================
# CONFUSION MATRIX
# ====================================

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

fig, ax = plt.subplots(
    figsize=(14, 14)
)

disp.plot(
    ax=ax,
    xticks_rotation=90
)

plt.title(
    "Resume Classification Confusion Matrix"
)

plt.show()

# ====================================
# SAVE MODEL
# ====================================

joblib.dump(
    model,
    "resume_classifier.pkl"
)

joblib.dump(
    vectorizer,
    "tfidf_vectorizer.pkl"
)

print(
    "\nModel saved successfully."
)
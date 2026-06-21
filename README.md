# Mini AI Projects

Three beginner-friendly Python projects demonstrating core AI/programming concepts: control flow, supervised learning basics, and recommendation logic.

## Requirements

- Python 3.8+
- `scikit-learn` and `pandas` (only needed for the classification model)

Install dependencies if needed:

```bash
pip install scikit-learn pandas
```

-----

## 1. Rule-Based Chatbot (`simple_chatbot.py`)

A chatbot that responds to predefined inputs using if-else logic in a continuous loop.

**Concepts:** Control flow, decision-making logic, basic AI concepts

**Features:**

- Handles greetings (`hi`, `hello`, `hey`)
- Answers simple questions (name, how are you)
- Exits on command (`bye`, `exit`, `quit`, `goodbye`)
- Runs in a continuous loop until the user exits

**Run it:**

```bash
python simple_chatbot.py
```

-----

## 2. Classification Model (`classification_model.py`)

Trains a K-Nearest Neighbors classifier on the Iris flower dataset to predict species from measurements.

**Concepts:** Data handling, supervised learning basics, model training

**Steps performed:**

1. Loads and previews the Iris dataset (150 samples, 4 features, 3 species)
1. Splits data into 80% training / 20% testing sets
1. Trains a KNN classifier (k=3)
1. Evaluates accuracy and prints a classification report
1. Runs a single sample prediction as a demo

**Run it:**

```bash
python classification_model.py
```

-----

## 3. Recommendation System (`recommendation_system.py`)

Recommends movies based on user-entered interests, using similarity scoring to rank matches.

**Concepts:** Logic building, pattern matching, recommendation concepts

**How it works:**

1. You enter your interests as comma-separated tags (e.g. `action, sci-fi`)
1. Each movie is scored using Jaccard similarity (shared tags ÷ total unique tags)
1. The top 3 highest-scoring movies are displayed

**Run it:**

```bash
python recommendation_system.py
```

-----

## Project Structure

```
.
├── simple_chatbot.py
├── classification_model.py
├── recommendation_system.py
└── README.md
```
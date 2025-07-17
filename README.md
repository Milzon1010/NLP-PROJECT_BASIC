# 🧠 NLP Streamlit Analyzer

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Tests](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/python-app.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions)

An interactive NLP dashboard built with **Streamlit, spaCy, NLTK**, and custom regex logic. Ideal for exploring text sentiment, entity recognition, and extracting patterns like hashtags, mentions, and URLs — all in real time.

---

## 🚀 Features

- 📊 **Sentiment Analysis** using NLTK VADER
- 🧠 **Named Entity Recognition** with spaCy
- 🔍 **Regex Pattern Extraction** for hashtags, mentions, URLs, numbers
- 💡 Modular code structure (`app/` folder)
- 🧪 Unit testing support via `pytest`

---

## 🧰 How to Run

From the root folder:

```bash
# Windows:
set PYTHONPATH=.
python -m streamlit run app/streamlit_app.py

# Linux/macOS:
PYTHONPATH=. streamlit run app/streamlit_app.py

📂 Project Structure
NLP-PROJECT_BASIC/
├── app/
│   ├── streamlit_app.py
│   ├── sentiment.py
│   ├── sentiment_utils.py
│   ├── ner_utils.py
│   ├── regex_utils.py
│   └── __init__.py
│
├── tests/
│   ├── test_sentiment.py
│   ├── test_ner.py
│   └── test_regex.py
│
├── requirements.txt
├── pytest.ini
└── README.md

🧪 Run Tests
pytest

🛠 Dependencies
Install dependencies:
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon
python -m spacy download en_core_web_sm

👤 Author
Built by Milzon — NLP enthusiast & AI explorer.

🌐 Deploy Streamlit to Cloud
Push this repo to GitHub

Go to streamlit.io/cloud and connect your repo

Use this as your app entry point:
app/streamlit_app.py

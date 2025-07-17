import streamlit as st
from app.sentiment_utils import get_sentiment_score
from app.ner_utils import extract_entities
from app.regex_utils import PATTERNS
import re
import sys
print("PYTHONPATH:", sys.path)

st.set_page_config(page_title="🧠 NLP Analyzer", layout="wide")
st.title("🧠 NLP Streamlit Analyzer")

# 📥 Input text
text = st.text_area("📝 Enter your text here:", height=220, value="""
Just launched our new #AI product! 🚀 Thanks to @team_awesome for the hard work. Check it out: https://oursite.com/product #innovation #tech

Beautiful sunset in San Francisco today 🌅 #photography #california #nature Love this city! @visit_sf

Apple just launched new iPhone with 50% more power and 12% better battery #Apple #iPhone 10,000 units sold on day one.
""")

# =========================================
# 🧠 NLP Processing Section
# =========================================
if text:

    # 🔍 Sentiment Analysis
    st.subheader("📊 Sentiment Analysis")
    sentiment = get_sentiment_score(text)
    st.json(sentiment)

    # 🧠 Named Entity Recognition
    st.subheader("🔎 Named Entity Recognition (spaCy)")
    entities = extract_entities(text)

    if entities:
        for ent_text, ent_label in entities:
            st.markdown(f"• **{ent_text}** — *{ent_label}*")
    else:
        st.info("No named entities found.")

    # 🧩 Regex Pattern Extraction
    st.subheader("🔍 Regex Pattern Extraction")
    for label, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            st.markdown(f"**{label.capitalize()}** (`{pattern}`):")
            st.code(matches, language="python")

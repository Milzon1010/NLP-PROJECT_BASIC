import spacy
from app.ner_utils import extract_entities


nlp = spacy.load("en_core_web_sm")

def test_ner_detection():
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    assert ("Apple", "ORG") in entities
from app.regex_utils import PATTERNS 
import re

def test_hashtags():
    text = "Loving #Python and #AI"
    matches = re.findall(PATTERNS['hashtags'], text)
    assert matches == ['#Python', '#AI']

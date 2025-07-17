from app.sentiment_utils import get_sentiment_score


def test_positive_sentiment():
    text = "I love this amazing experience!"
    score = get_sentiment_score(text)
    assert score['compound'] > 0.5
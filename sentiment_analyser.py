import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def initialisation():
    nltk.download('vader_lexicon')
    nltk.download('punkt_tab')


def analyze(string: str):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(string)


def tokenize(line: str, language: str = "english"):
    return nltk.word_tokenize(line, language)


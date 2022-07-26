from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer


def sumarize(url: str, sentences: int) -> None:
    LANGUAGE = "english"
    SENTENCES_COUNT = sentences
    url = url
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

    summarizer = LuhnSummarizer()
    summarizer = LuhnSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = (
        "I",
        "am",
        "the",
        "you",
        "me",
        "is",
        "than",
        "that",
        "this",
    )

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)


def main():
    url = input("Enter url: ")
    sentences = int(input("Enter number of sentences: "))

    sumarize(url, sentences)


if __name__ == "__main__":
    main()

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summarize_text(text, sentence_count=3):
    if not text.strip():
        return "❌ Error: Input text is empty."

    # Prepare the parser
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize the summarizer
    summarizer = LexRankSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentence_count)

    # Join the sentences
    return "\n".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    print("📘 TEXT SUMMARIZATION TOOL (Extractive)\n")
    input_text = input("Paste your article here:\n\n")

    print("\n📄 SUMMARY:\n")
    result = summarize_text(input_text, sentence_count=3)
    print(result)

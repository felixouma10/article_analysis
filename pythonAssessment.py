import re
from collections import Counter


def count_specific_word(text, search_word):
    """Count occurrences of a word or substring in the text."""
    if not search_word:
        return 0

    return text.lower().count(search_word.lower())


def identify_most_common_word(text):
    """Return the most common word, or None if the text is empty."""
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return None

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """Calculate average word length, excluding punctuation."""
    words = re.findall(r"\b\w+\b", text)

    if not words:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    """Count paragraphs separated by one or more empty lines."""
    if not text.strip():
        return 1

    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len(paragraphs)


def count_sentences(text):
    """Count sentences ending in ., !, or ?."""
    if not text.strip():
        return 1

    sentences = re.findall(r"[.!?]+(?=\s|$)", text.strip())
    return len(sentences)


def main():
    # Read the news article from a text file.
    try:
        with open("news_article.txt", "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt was not found.")
        return

    # Display the analysis menu.
    while True:
        print("\n NEWS ARTICLE ANALYZER")
        print("1. Count a specific word")
        print("2. Identify the most common word")
        print("3. Calculate average word length")
        print("4. Count paragraphs")
        print("5. Count sentences")
        print("6. Display all analysis results")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_word = input("Enter the word to search for: ")
            result = count_specific_word(article, search_word)
            print(f"Occurrences of '{search_word}': {result}")

        elif choice == "2":
            print("Most common word:",
                  identify_most_common_word(article))

        elif choice == "3":
            print("Average word length:",
                  calculate_average_word_length(article))

        elif choice == "4":
            print("Number of paragraphs:", count_paragraphs(article))

        elif choice == "5":
            print("Number of sentences:", count_sentences(article))

        elif choice == "6":
            print("\n ANALYSIS RESULTS ")
            print("Most common word:",
                  identify_most_common_word(article))
            print("Average word length:",
                  calculate_average_word_length(article))
            print("Number of paragraphs:", count_paragraphs(article))
            print("Number of sentences:", count_sentences(article))

            search_word = input("Enter a word to count: ")
            print("Word occurrences:",
                  count_specific_word(article, search_word))

        elif choice == "0":
            print("Thank you for using the News Article Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
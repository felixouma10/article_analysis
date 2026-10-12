# Project: Article_Analysis

## Project Overview

This project is a Python program that analyzes a news article and provides useful statistics about its content. It reads an article from a text file and allows users to perform different text analysis operations through an interactive menu.

The project demonstrates the use of Python functions, strings, regular expressions, dictionaries, loops, conditional statements, and file handling.

## Features

- **Specific Word Count:** Counts how many times a specified word or substring appears in the article, regardless of letter case.
- **Most Common Word:** Identifies the word that occurs most frequently in the article.
- **Average Word Length:** Calculates the average length of words in the article, excluding punctuation.
- **Paragraph Count:** Counts paragraphs separated by blank lines.
- **Sentence Count:** Counts sentences ending with periods, exclamation marks, or question marks.
- **Interactive Menu:** Allows users to select different analysis options using a `while` loop.
- **Input Validation:** Uses conditional statements to handle menu choices and invalid selections.
- **File Handling:** Reads article content from `news_article.txt`.

## Project Structure

```text
Analyze-a-News-Article/
├── pythonAssessment.py
├── news_article.txt
└── README.md
```

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- Collections Module (`Counter`)
- File Handling
- Command-Line Interface (CLI)

## Requirements

- Python 3 installed on your computer.
- The `pythonAssessment.py` and `news_article.txt` files saved in the same project directory.
- The Python standard libraries `re` and `collections`.

No external Python packages are required for this project.

## How to Run the Program

### 1. Clone or download the project

Download the project files to your computer.

### 2. Navigate to the project directory

Open your terminal and navigate to the folder containing the Python script and article file.

```bash
cd article_analysis
```

### 3. Run the program

```bash
python3 pythonAssessment.py
```

### 4. Interact with the menu

Follow the instructions displayed in the terminal to select an analysis operation. Enter the requested information when prompted.

Ensure that `news_article.txt` is in the correct directory so the program can read the article.

## Functions Implemented

| Function | Description |
|---|---|
| `count_specific_word(text, search_word)` | Counts occurrences of a specified word or substring. |
| `identify_most_common_word(text)` | Returns the most frequently occurring word, or `None` if there are no words. |
| `calculate_average_word_length(text)` | Returns the average word length, or `0` if there are no words. |
| `count_paragraphs(text)` | Counts paragraphs separated by blank lines. |
| `count_sentences(text)` | Counts sentence-ending punctuation marks. |

## Python Concepts Demonstrated

- **Functions:** Breaks the program into reusable blocks of code.
- **Strings:** Processes and analyzes text.
- **Regular Expressions:** Extracts words and identifies sentence endings.
- **Loops:** Uses `while` for the interactive menu and `for` to iterate through words or other data.
- **Conditional Statements:** Uses `if`, `elif`, and `else` to control program flow.
- **File Handling:** Opens and reads the news article from a text file.
- **Error and Empty-Input Handling:** Handles cases such as empty text and invalid menu choices.

## Learning Objectives

The objective of this project is to apply fundamental Python programming concepts to a practical text-processing problem. It provides experience in writing reusable functions, manipulating strings, reading files, and building a command-line application.

## Author

Felix Ouma.

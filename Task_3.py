import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

output_txt_file = 'merged_texts.txt'
top_words_csv = 'top_30_words.csv'

# Task 3.1: Count the Top 30 Most Common Words and Store in a CSV File
def count_top_words(text_file, output_csv):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Split the text into words and count occurrences
        words = text.split()
        word_counts = Counter(words)

        # Get the 30 most common words
        top_30_words = word_counts.most_common(30)

        # Store the result in a CSV file
        df_top_words = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
        df_top_words.to_csv(output_csv, index=False)

        print(f"\nTask 3.1: Top 30 words saved to {output_csv}\n")
    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred while counting words: {str(e)}")

# Task 3.2: Count Unique Tokens Using Transformers AutoTokenizer
def count_unique_tokens(text_file):
    try:
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)

        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text using AutoTokenizer
        tokens = tokenizer.tokenize(text)

        # Count token occurrences
        token_counts = Counter(tokens)

        # Get the 30 most common tokens
        top_30_tokens = token_counts.most_common(30)
        
        print(f"\nTask 3.2: Top 30 tokens:\n {top_30_tokens}")
        return top_30_tokens

    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred while counting tokens: {str(e)}")

# Run the function for Task 3.1
count_top_words(output_txt_file, top_words_csv)

# Run the function for Task 3.2
count_unique_tokens(output_txt_file)

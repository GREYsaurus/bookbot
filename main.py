from stats import count_words, character_frequency  # Import functions from stats.py

def get_book_text(filepath):
    """
    Reads the content of a file and returns it as a string.
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The specified file was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    """
    Reads the content of frankenstein.txt, calculates word count and character frequencies,
    and prints the results to the console.
    """
    filepath = "books/frankenstein.txt"  # Relative path to the file
    book_content = get_book_text(filepath)

    if "Error:" not in book_content:  # Check if the file was successfully read
        word_count = count_words(book_content)  # Get the word count
        print(f"{word_count} words found in the document")
        
        char_freq = character_frequency(book_content)  # Get character frequencies
        print("\nCharacter Frequencies:")
        print(char_freq)
    else:
        print(book_content)  # Print the error message if the file could not be read

# Example usage
if __name__ == "__main__":
    main()
import sys
from stats import count_words, character_frequency, sorted_character_frequency  # Import functions from stats.py

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
    Reads the content of a user-specified book file, calculates word count and sorted character frequencies,
    and prints the report in the specified format.
    """
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program with an error status

    filepath = sys.argv[1]  # Get the file path from the command line argument
    book_content = get_book_text(filepath)

    if "Error:" not in book_content:  # Check if the file was successfully read
        word_count = count_words(book_content)  # Get the word count
        char_freq = character_frequency(book_content)  # Get character frequencies
        sorted_freq = sorted_character_frequency(char_freq)  # Sort and filter character frequencies
        
        # Print the formatted report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        for entry in sorted_freq:
            print(f"{entry['character']}: {entry['count']}")

        print("============= END ===============")
    else:
        print(book_content)  # Print the error message if the file could not be read

# Run the script
if __name__ == "__main__":
    main()
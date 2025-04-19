import sys
from stats import count_words, character_frequency, sorted_character_frequency  

def get_book_text(filepath):
  
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The specified file was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
  
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  

    filepath = sys.argv[1]  
    book_content = get_book_text(filepath)

    if "Error:" not in book_content:  
        word_count = count_words(book_content)  
        char_freq = character_frequency(book_content)  
        sorted_freq = sorted_character_frequency(char_freq)  
        
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        for entry in sorted_freq:
            print(f"{entry['character']}: {entry['count']}")

        print("============= END ===============")
    else:
        print(book_content)  


if __name__ == "__main__":
    main()
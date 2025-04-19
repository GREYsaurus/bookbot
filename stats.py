def count_words(text):
    """
    Counts the number of words in a given string.
    """
    words = text.split()  # Split the text into words using whitespace
    return len(words)  # Return the number of words

def character_frequency(text):
    """
    Counts the frequency of each character in the given string,
    including symbols and spaces, and returns a dictionary.
    """
    text = text.lower()  # Convert text to lowercase to avoid duplicates
    frequency = {}  # Initialize an empty dictionary for character frequencies
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency  # Return the dictionary containing character frequencies

def sorted_character_frequency(char_freq):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Filters out non-alphabetical characters and sorts from greatest to least count.
    """
    # Convert dictionary into a list of dictionaries with only alphabetical characters
    filtered_list = [{"character": char, "count": count} for char, count in char_freq.items() if char.isalpha()]
    
    # Sort the list in descending order based on count
    filtered_list.sort(key=lambda x: x["count"], reverse=True)
    
    return filtered_list
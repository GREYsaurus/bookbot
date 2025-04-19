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
    
    for char in text:  # Iterate through each character in the text
        if char in frequency:  # Increment the count for the character
            frequency[char] += 1
        else:
            frequency[char] = 1  # Add the character to the dictionary
    
    return frequency  # Return the dictionary containing character frequencies
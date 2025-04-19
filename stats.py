def count_words(text):
   
    words = text.split()  
    return len(words)  

def character_frequency(text):
   
    text = text.lower()  
    frequency = {}  
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency  

def sorted_character_frequency(char_freq):
   
    filtered_list = [{"character": char, "count": count} for char, count in char_freq.items() if char.isalpha()]
    
   
    filtered_list.sort(key=lambda x: x["count"], reverse=True)
    
    return filtered_list
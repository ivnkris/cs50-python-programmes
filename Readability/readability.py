from cs50 import get_string


def main():
    # Get some text from the user
    text = get_string("Text: ")
    
    # Count the letters in the text
    letters = count_letters(text)
    
    # Count the words in the text
    words = 0
    # If text isn't empty start word count from 1
    if letters > 0:
        words = 1
        
    words += count_words(text)
    
    # Count the sentences in the text
    sentences = count_sentences(text)
    
    # Count readability score
    readability_score = count_readability_score(letters, words, sentences)
    
    # Print readability grade
    if readability_score < 1:
        print("Before Grade 1")
    elif readability_score > 16:
        print("Grade 16+")
    else:
        print(f"Grade {readability_score}")
        

def count_letters(s):
    letters = 0
    for i in range(len(s)):
        # If the character is either an uppercase or lowercase letter, increase the count
        if s[i].isalpha():
            letters += 1
    return letters
    
    
def count_words(s):
    words = 0
    # Iterate through text and if found a space count it as word
    for i in range(len(s)):
        if s[i] == " ":
            words += 1
    return words
    

def count_sentences(s):
    sentences = 0
    # Iterate through text and if found . or ! or ? count it as sentence
    for i in range(len(s)):
        if s[i] == "." or s[i] == "!" or s[i] == "?":
            sentences += 1
    return sentences
    

def count_readability_score(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    # Calculate Coleman-Liau index
    index = 0.058 * L - 0.296 * S - 15.8
    # Round to nearest integer
    score = round(int(index)) + 1
    
    return score
    

# Run programme
if __name__ == "__main__":
    main()
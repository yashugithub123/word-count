def word_counter(text):
    try:
        # Check if the input is a string
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Remove leading and trailing whitespaces
        text = text.strip()
        
        # Check if the text is empty
        if not text:
            return 0
        
        # Split the text into words using whitespace as separator
        words = text.split()
        
        # Return the count of words
        return len(words)
    
    except TypeError as e:
        # Handle TypeError
        print("Error:", e)
        return -1

# Example text
input_text = "This is a sample text for word counting."
    
# Call the function and print the result
count = word_counter(input_text)
    
if count != -1:
    print("Number of words:", count)
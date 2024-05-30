def word_counter(text):
    words = text.split()
    return len(words)

text = input("Enter the text: ")
print("Number of words:", word_counter(text))
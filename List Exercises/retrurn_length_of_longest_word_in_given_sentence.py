'''Write a Python function that takes a list of words and returns the length of the longest one. '''

def longest_word(sentence):
    words = sentence.split()
    length_words = [len(i) for i in words]
    return words[length_words.index(max(length_words))]

sentence = input("Enter a sentence: ")
print("Longest word: "+longest_word(sentence))
print("Length: "+str(len(longest_word(sentence))))

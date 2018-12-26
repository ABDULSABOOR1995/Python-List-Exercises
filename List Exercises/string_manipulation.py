'''Write a Python program to count the number of strings where
    the string length is 2 or more and the first and last character
    are samefrom a given list of strings.'''

def give_str(words):
    selected_words = []
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            selected_words.append(word)
    return selected_words

words = ['abc','xyz','aba','1221']
print(give_str(words))
print("No of selected_words: "+str(len(give_str(words))))


'''Write a Python program to find the list of words that are longer
   than n from a given list of words.'''
def give_words(sentence, num):
    words_greaterthan_n = []
    words = sentence.split()
    for word in words:
        if len(word) > num:
            words_greaterthan_n.append(word)
    return words_greaterthan_n
    
    

sentence = input("Enter a sentence: ")
num = int(input("Enter a no: "))
print(give_words(sentence, num))


'''Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.'''

string = input("Enter an string: ")
chars = []
for i in range(0, len(string)):
    if string[i] not in chars:
        chars.append(string[i])
    else:
        first_repeated_word = string[i]
        index = string.index(first_repeated_word)
        break
print("The first repeated character is: "+first_repeated_word+" whose index is "+str(index)) 

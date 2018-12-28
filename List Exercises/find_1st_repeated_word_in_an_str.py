'''Write a Python program to find the first repeated word in a given string.'''

string = input("Enter an string: ")
chars = []
for i in string:
    if i not in chars:
        chars.append(i)
    else:
        first_repeated_word = i
        break
print("The first repeated character is: "+first_repeated_word) 

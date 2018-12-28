'''Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2'''
string = input("Enter an string: ")
unique_letters = []
unique_letters_occurence = []
for i in string:
    if i not in unique_letters:
        unique_letters.append(i)

for i in unique_letters:
    n = 0
    for j in string:
        if i == j:
            n+= 1
    unique_letters_occurence.append(n)

for i in range(0,len(unique_letters_occurence)):
    if unique_letters_occurence[i] > 1:
        print(unique_letters[i]+": "+str(unique_letters_occurence[i]))

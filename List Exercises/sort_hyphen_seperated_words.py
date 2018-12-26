'''Write a Python program that accepts a hyphen-separated sequence of words as
input and prints the words in a hyphen-separated sequence after sorting them
alphabetically.'''
input_value = "green-red-yellow-black-white"
colors = input_value.split("-")
colors.sort()
s = ''
for i in colors:
    s+= i+"-"
    
letters = list(s)
del(letters[-1])
s = ''
for i in letters:
    s+= i
print(s)

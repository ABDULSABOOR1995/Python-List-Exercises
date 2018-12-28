''' Write a Python program to remove the characters which have odd index values of a given string.'''

sentence = input("Enter a sentence: ")
odd_letters = ''
result = [sentence[i] for i in range(1,len(sentence),2)]
for i in result:
	odd_letters+= i
print(odd_letters)


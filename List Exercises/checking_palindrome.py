'''Write a Python function to check whether a string is a palindrome or not.'''
string = input("Enter an string: ")
reverse = ''
for i in range(len(string)-1, -1, -1):
    reverse+= string[i]
if string == reverse:
    print("Palindrome")
else:
    print("not a palindrome")

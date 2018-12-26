'''Write a Python function to check whether a string is a pangram or not.'''
alphabets = list("abcdefghigklmnopqrstuvwxyz")
alphabets
sentence = "the quick brown fox jumps over the lazy dog"
letters = set(sentence)
result = True
for i in alphabets:
    if i not in letters:
        result = False
        break
if result:
    print("Pangram")
else:
    print("not a pangram")

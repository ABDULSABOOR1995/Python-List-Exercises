'''Write a Python program to find the maximum occurring character in a given string.'''


string = input("Enter an string: ")
chars = []
count = []
for i in string:
    if i not in chars:
        chars.append(i)

for i in chars:
    n = 0
    for j in list(string):
        if i == j:
            n+= 1
    count.append(n)
    print(i+": "+str(n))
max_index = count.index(max(count))
print("Miximum occuring chartacter is "+chars[max_index]+" which occurs "+str(count[max_index])+" times")
        

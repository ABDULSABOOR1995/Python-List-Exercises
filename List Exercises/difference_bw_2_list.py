'''Write a Python program to get the difference between the two lists.'''
list_1 = [6,7,8,9,10]
list_2 = [1,3,5,7,9]
difference = []
for i in range(0 ,len(list_1)):
    difference.append(list_1[i] - list_2[i])
    
print(difference)

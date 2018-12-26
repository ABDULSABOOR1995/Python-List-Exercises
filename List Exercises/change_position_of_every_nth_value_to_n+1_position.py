'''Write a Python program to change the position of every n-th value with the
    (n+1)th in a list.'''

list_num = [0,1,2,3,4,5]
for i in range(0, len(list_num)):
    if i % 2 == 0:
        temp = list_num[i]
        list_num[i] = list_num[i+1]
        list_num[i+1] = temp
        

print(list_num)

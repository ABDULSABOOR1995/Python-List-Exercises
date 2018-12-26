'''Write a program that sort a list in descending order '''

n = [9,2,8,1,10,34,1,4,37,2]
for i in range(0, len(n)):
    for j in range(i+1, len(n)):
        if n[i] < n[j]:
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
print(n)   

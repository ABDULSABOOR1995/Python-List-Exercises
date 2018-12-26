'''Write a Python program to create a list by concatenating a given list which
range goes from 1 to n.
i.e Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''
sample_list = ['p','q']

n = int(input("Enter range:  "))
making_list  =[j+str(i) for i in range(1, n+1)  for j in sample_list] 
print(making_list)

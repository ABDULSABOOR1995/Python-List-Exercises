'''Write a Python program to print the numbers of a specified list after
       removing even numbers from it.'''

no_list = [24,77,62,33,12,11,78,99,90]
print("Before removing evens\n"+str(no_list))
no_list= [i for i in no_list if i % 2!= 0]
print("After removing evens")
print(no_list)

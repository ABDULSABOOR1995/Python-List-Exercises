'''Write a Python program to generate and print a list of first and last 5
       elements where the values are squareof numbers between 1 and 30
       (both included).'''
       
nums = [i**2 for i in range(1, 31)]
first_5_elements = nums[:5]
last_5_elements = nums[-1:-6:-1]
last_5_elements.reverse()
first_and_last_5_elements = first_5_elements + last_5_elements
print(first_and_last_5_elements)

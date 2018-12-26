'''Write a Python program to generate and print a list except for the first 5
   elements, where the values are square of numbers between 1 and 30 
   (both included).'''
   
nums = [i**2 for i in range(1, 31)]
list_except_1st_5_elements  = nums[5:]
print(list_except_1st_5_elements)

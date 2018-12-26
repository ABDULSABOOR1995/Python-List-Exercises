'''Write a Python program to find missing and additional values in two lists.'''
list_1 = ['a','b','c','d','e','f']
list_2 = ['d','e','f','g','h']
missing_values_in_list_2 = [i for i in list_1 if i not in list_2]
additional_values_in_list_2 = [i for i in list_2 if i not in list_1]
print("Missing values in list 2: "+str(missing_values_in_list_2))
print("Additional values in list 2: "+str(additional_values_in_list_2))

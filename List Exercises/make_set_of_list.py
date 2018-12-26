'''Write a Python function that takes a list and returns a new list with unique
    elements of the first list.'''
num_list = [1,2,2,2,3,3,4,4,4,4,5,5,5,5,5]
set(num_list) # is se set ban raha h list nahei ban rahi
'''for making list'''
unique_elements = []
for i in num_list:
    if i not in unique_elements:
        unique_elements.append(i)
print(unique_elements)

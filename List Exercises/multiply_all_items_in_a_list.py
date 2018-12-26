'''Write a Python program to multiplies all the items in a list.'''

def mul_items(items):
    mul = 1
    for item in items:
        mul *= item
    return(mul)

items = [-12,-22,-5,-7]
print(mul_items(items))

'''Write a Python function that takes two lists and returns True if they have
       at least one common member.'''

def check_common_member(list_1, list_2):
    common = False
    for i in list_1:
        if i in list_2:
            common = True
            break
    return common

list_1 = [1,2,3,4,5]
list_2 = [5,6,7,8,9]
print(check_common_member(list_1, list_2))

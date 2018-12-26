'''Write a Python program to find the index of an item in a specified list.'''

nums = [10,20,30,40,50,60,70,80,90]
index = 0
for i in range(0, len(nums)):
    if nums[i] == 50:
        index = i
        
print(index)

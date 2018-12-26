'''Write a Python program to find a pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4'''

numbers= [10,20,10,40,50,60,70]
pair_indices = []
for i in range(0, len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 50:
            pair_indices.append(i)
            pair_indices.append(j)
            
import numpy as np
pair_indices = np.array(pair_indices).reshape(2,2)
print(pair_indices)

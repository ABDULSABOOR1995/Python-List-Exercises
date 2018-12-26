'''Write a Python program to find the three elements that sum to zero
   from a set of n real numbers.'''

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
sets = []
complete_set = []
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                sets.append(nums[i])
                sets.append(nums[j])
                sets.append(nums[k])
import numpy as np
sets = np.array(sets).reshape(2,3)
print(sets)

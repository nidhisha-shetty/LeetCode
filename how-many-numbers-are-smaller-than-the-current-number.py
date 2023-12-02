'''
P.S: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
'''

#Solution 1:
res = []
for num in nums:
    count = 0
    for num1 in nums:
        if num1 < num:
            count+=1
    res.append(count)
return res

#Solution 2:
sorted_nums = sorted(nums)
result = [sorted_nums.index(i) for i in nums]
return result

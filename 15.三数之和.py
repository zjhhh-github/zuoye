# -*- coding:utf-8 -*-
nums = [-1,0,1,2,-1,-4]

nums.sort()
result = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left = i + 1
    right = len(nums) - 1
    while left < right:
        node = nums[i] + nums[left] + nums[right]
        if node > 0:
            right -= 1
        elif node < 0:
            left += 1
        else:
            result.append([nums[i],nums[left],nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
print(result)
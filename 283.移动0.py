# -*- coding:utf-8 -*-
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
nums = [0,0,1]
# i = 0
# n = 0
# while nums:
#     if nums[i] == 0:
#         nums[i:len(nums) - 1] = nums[i+1:]
#         nums[-1] = 0
#         n += 1
#     elif nums[i] != 0:
#         i += 1
#     if n > len(nums) or i == len(nums):
#         break

s = 0
f = 0
while f < len(nums):
    if nums[f] == 0:
        f += 1
    else:
        nums[s],nums[f] = nums[f],nums[s]
        s += 1
        f += 1
print(nums)
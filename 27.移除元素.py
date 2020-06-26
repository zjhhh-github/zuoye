# -*- coding:utf-8 -*-
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
nums = [1,1,2,3]
# val = 1
# n = len(nums)
# i = 0
# while nums:
#     if nums[i] == val:
#         nums[i:len(nums) - 1] = nums[i+1:]
#         nums[-1] = [None]
#         n -= 1
#     elif i == len(nums) - 1:
#         break
#     else:
#         i += 1
class Solution:
    def removeElement(self,nums,val:int):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow

print(nums)
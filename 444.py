# -*- coding:utf-8 -*-
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        f = 1
        while f < len(nums):
            if nums[f] == nums[s]:
                f += 1
            else:
                s += 1
                nums[s] = nums[f]
                f += 1
        return s + 1
Solution([1,1,2,3,3,5,3])
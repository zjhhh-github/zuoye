# -*- coding:utf-8 -*-
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
nums = [1,1,1,1,2,2,3,3,3]
# i = 0
# n = len(nums)
# for i in range(len(nums)):
#     c = 0
#     j = i + 1
#     while nums:
#         if j == len(nums) or nums[i] == None:
#             break
#         if nums[i] == nums[j]:
#             c += 1
#             if c > 1:
#                 nums[j:len(nums) -1] = nums[j+1:]
#                 nums[-1] = None
#                 n -= 1
#                 j -= 1
#             j += 1
#         else:
#             j += 1
i = 0
j = i + 1
n = len(nums)
c = 1
while i < len(nums) - 2 and nums[i] != None:
    print(i,j,c,nums)
    if j == len(nums):
        i += 1
        c = 1
        j = i + 1
        continue
    elif nums[i] == nums[j]:
        c += 1
    if c > 2:
        nums[j:len(nums) -1] = nums[j+1:]
        j -= 1
        n -= 1
        c = 2
        nums[-1] = None
    j += 1



print(nums,n)
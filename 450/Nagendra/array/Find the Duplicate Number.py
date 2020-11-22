
from collections import defaultdict
                         #### time nlogn, space 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]



               ### time n,space n
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            if dic[i] == 1:
                return i
            dic[i] = 1


            ### Hare and tortoise approach BEST time n, space 1

class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tor = hare = nums[0]

        while True:
            tor = nums[tor]
            hare = nums[nums[hare]]
            if tor == hare:
                break
        tor = nums[0]

        while tor != hare:
            tor = nums[tor]
            hare = nums[hare]

        return hare



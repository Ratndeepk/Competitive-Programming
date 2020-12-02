# Finding duplicate in array in O(n) time & O(1) space

"""
Trick:
Treat your array as linkedlist & find first element of loop
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast=nums[0]
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow==fast:
                break 
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast=nums[fast]
            
                
        return slow

s = Solution()
arr = list(map(int,input().split()))
print(s.findDuplicate(arr))
#link https://leetcode.com/problems/search-in-rotated-sorted-array/
#linear search
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

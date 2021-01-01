#link https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr=list()
        intervals.sort(key= lambda x:x[0])
        
        for i in intervals:
            if not arr or arr[-1][1]<i[0]:
                arr.append(i)
            else:
                arr[-1][1]= max(i[1], arr[-1][1])
        
        return arr
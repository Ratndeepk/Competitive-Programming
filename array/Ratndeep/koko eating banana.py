import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        x = math.ceil(sum(piles)/H)
        while True:
            time=0
            for i in piles:
                time+=math.ceil(i/x)
            if time<=H:
                break
            else:
                x+=1
        return x

#find the dublicates
def duplicate(num):
    s=f=num[0]
    while True:
        s=num[s]
        f=num[num[f]]
        if s==f:
            break
    s=num[0]
    while s!=f:
        s=num[s]
        f=num[f]
    print(f)

#drivers code
num=list(map(int,input().split()))
duplicate(num)

'''class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare'''

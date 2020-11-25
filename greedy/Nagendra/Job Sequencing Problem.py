#code link - https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0
# SOLN 1
for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    for i in range(0, n*3, 3):
        dic[i] = arr[i+1:i+3]
    arr = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
    profit_arr = [0]*n
    c = 0
    for i in arr:
        for j in range(min(n-1, i[1][0]), -1, -1):
            if profit_arr[j] == 0:
                if i[1][0] >= j+1:
                    profit_arr[j] = i[1][1]
                    c += 1
                    # print(profit_arr)
                    break
                
    print(c,sum(profit_arr))

#SOLN 2

class Sequence:

    def __init__(self,d,p):
        self.d = d 
        self.p = p
    def __lt__(self,other):
        return self.p < other.p

for _ in range(int(input())):

    n= int(input())
    arr = list(map(int, input().split()))
    sorted_arr =[]

    for i in range(0, n*3, 3):
        sorted_arr.append(Sequence(arr[i+1],arr[i+2]))
    sorted_arr.sort(reverse=True)
    profit_arr=[0]*n
    c=0
    for i in sorted_arr:
        for j in range(min(n-1,i.d),-1,-1):
            if profit_arr[j]==0:
                if i.d >= j+1:
                  profit_arr[j] = i.p
                  c+=1
                  break
    print(c, sum(profit_arr))



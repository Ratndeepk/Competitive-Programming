#User function Template for python3

def largestNum(n,s):
    '''
    :param n: length of given numberr
    :param s: sum of digits of number
    :return: Integer
    '''
    # code here
    pwd=""
    for i in range(n):
        if s>=9:
            pwd+='9'
            s-=9
        elif s==0:
            pwd+='0'
        else:
            pwd+=str(s)
            s=0
    if s!=0:
        return -1
    return int(pwd)
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        print(largestNum(n,s))
# } Driver Code Ends
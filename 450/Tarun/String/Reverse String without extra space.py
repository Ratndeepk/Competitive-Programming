#Reverse String without extra space
def reverseString(s):
        n = len(s)
        if n == 1:
            pass
        else:
            if n%2==1:
                mid = n//2
                i,j = mid-1,mid+1
            else:
                i,j = (n//2)-1 ,n//2
            while(i >= 0 and j < n):
                s[i],s[j] = s[j],s[i]
                i -= 1
                j += 1
        print(s)
s = ["h","e","l","l","o"]
reverseString(s)
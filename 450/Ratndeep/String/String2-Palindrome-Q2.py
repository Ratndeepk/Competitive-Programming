def isPlaindrome(self, S):

    start=0
    end=len(S)-1 
    while start<end:
	if S[start]!=S[end]:
	    return 0 
	start+=1 
	end-=1 
    return 1


S = input()
if isPalindrome(S):
    print("yes")
else:
    print("no")

def subset(array,n,ans):
    subs = [None]*n
    helper(n,array,subs,0,ans)
    return ans
def helper(n,array,subs,i,ans):
    if i==n:
        lis=[]
        if any(subs):
            for j in range(len(subs)):
                if subs[j]!=None:
                    lis.append(subs[j])
            ans.append(lis)
            

    else:
        subs[i]=None
        helper(n,array,subs,i+1,ans)
        subs[i]=array[i]
        helper(n,array,subs,i+1,ans)
        

ans=[]
a = subset([1,2,3],3,ans)
print(a)

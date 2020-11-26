def maxSubArraySum(a,size):
    ##Your code here
    cur_sum=0
    max_sum=0 
    i=0
    while i<size:
        cur_sum+=a[i]
        if cur_sum<0:
            cur_sum=0
        if cur_sum>max_sum:
            max_sum=cur_sum 
        
        i+=1
    return max_sum
    
def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    # code here
    st=[]
    for i in range(n):
        st.append([start[i],end[i]])
        
    st.sort(key=lambda x:x[1])
    
    if len(st)==1:
        return 1 
        
    count=0
    j=0
    last=0
    while j<len(st):
        cur = st[j][0]
        if last<=cur:
            count+=1 
            last=st[j][1]
        j+=1
            
        
    return count
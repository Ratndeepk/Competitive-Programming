def maximumMeetings(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    # code here
    meeting = []
    for i in range(n):
        meeting.append([start[i],end[i],i])
        
    meeting.sort(key=lambda x:x[1])
    count,time=[],0
    for i in range(n):
        cur_time=meeting[i][0]
        if time<cur_time:
            time = meeting[i][1]
            count.append(meeting[i][2]+1)
    print(*count) 

    
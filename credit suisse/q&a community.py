import collections
# Participants may update the following function parameters
def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    flat_list = [item for sublist in questionAndAnswerListOfList for item in sublist]
    n = max(len(questionAndAnswerListOfList),max(flat_list))
    dic=dict.fromkeys(range(1,n+1),[0])
    sus=[] 
    
    for i in questionAndAnswerListOfList:
        dic[i[0]]=i[1:]
    #print(dic)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and dic[i]!=[0]:
                if (j in dic[i] and i in dic[j]):
                    #print("Here1")
                    if i not in sus:
                        sus.append(i)
                        break
                elif len(list(set(dic[i]) & set(sus)))>=2:
                    #print("here 2")
                    if i not in sus:
                        sus.append(i) 
                        break
                else:
                    #print("Here")
                    count=0
                    #print(dic[i])
                    for k in dic[i]:
                        #print(count,dic[k])
                        
                        if k in sus:
                            count+=1 
                        elif len(list(set(dic[k]) & set(sus)))>=2:
                            count+=1 
                        if count>=2:
                            if i not in sus:
                                sus.append(i)
                            break
                        
    sol=""
    if sus!=[]:
        for i in sus:
            sol+=str(i)+","
        return sol[:len(sol)-1]
    return " "


    """
    #print(dic)
    matrix = [[False for i in range(n+1)] for i in range(n+1)]
    #for i in matrix:
    #    print(*i)
    
    for i in range(1,n+1):
        index=0
        for j in range(1,n+1):
            if index<len(dic[i]):
                if j==dic[i][index]:
                    matrix[i][j]=True
                    index+=1
    #print()
    #for i in matrix:
    #    print(*i)

    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if matrix[i][j]==True and matrix[j][i]==True:
                sus.append(i) 
            elif matrix[i][j]==True:
                if j in sus:
                    count+=1 
                else: 
                    if len(set(dic[j])&set(sus))>=2:
                        count+=1  
            if count>=2:
                sus.append(i)
                break

    sol=""
    if sus!=[]:
        for i in sus:
            sol+=str(i)+","
        return sol[:len(sol)-1]
    return sol 
    """
def main():
    firstLine = input().split(" ")
    secondLine = input()

    # Sample input:
    # 3
    # 1 2,2 1,3 1 2

    numOfQuestions = int(firstLine[0])
    questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = parseQuestionAndAnswer(questionAndAnswers)

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parseQuestionAndAnswer(questionAndAnswers):
    questionAndAnswerListOfList = []
    for index in range(0, len(questionAndAnswers)):
        questionAndAnswerList = questionAndAnswers[index].split(" ")
        questionAndAnswerListOfList.append([int(x) for x in questionAndAnswerList])
    return questionAndAnswerListOfList


if __name__ == '__main__':
    main()
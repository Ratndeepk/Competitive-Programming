import collections

def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    n = numOfQuestions 
    qa = questionAndAnswerListOfList 
    graph={}
    for i in questionAndAnswerListOfList:
        graph[i[0]]=i[1:]
    sol=[]
    queue=[]
    matrix = [[False for i in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1): 
        for j in range(1,n+1):
            try:
                if j in graph[i] and i in graph[j]:
                    matrix[i][j]=True 
                    if i not in sol:
                        sol.append(i)
                if j in graph[i]:
                    matrix[i][j]=True
                    
            except KeyError:
                pass  

    #for i in matrix:
    #    print(*i)
    while(True):
        x=len(sol)
        for i in range(1,n+1): 
            count=0
            for j in range(1,n+1):
                if matrix[i][j]==True and matrix[j][i]==False: 
                    if j in sol:
                        count+=1 
                    if count>=2 and i not in sol:
                        sol.append(i)
                        break  
        if len(sol)==x:
            break        

    sol.sort()
    answer=""
    if sol!=[]:
        for i in sol:
            answer+=str(i)+","
        return answer[:len(answer)-1]
    return answer








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
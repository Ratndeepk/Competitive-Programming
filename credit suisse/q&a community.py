import collections
# Participants may update the following function parameters

def dfs(x,graph,visited,count,flag):
    if flag==0:
        for i in graph[x]:
            try:
                if x in graph[i]:
                    visited[x]=True 
                    return 
            except KeyError:
                pass 
    
    flag=1
    try:
        if graph[x]:
            pass 
    except KeyError:
        return 0
    for i in graph[x]:
        if count[0]>=2:
            break
        if visited[i]==True:
            count[0]+=1  
            continue 


        if dfs(i,graph,visited,count,flag)==0:
            continue
        dfs(x, graph, visited, count, flag)
        
        return 
            
    return 
def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    
    graph={}
    for i in questionAndAnswerListOfList:
        graph[i[0]]=i[1:]
    n = len(questionAndAnswerListOfList)
    visited=[False]*(10000)
    for i in range(1,10000):
        count=[0]
        try:
            if graph[i]:
                dfs(i,graph,visited,count,0)
        except KeyError:
            continue 
        if count[0]>=2:
            visited[i]=True
    solution=""
    for i in range(1,10000):
        if visited[i]==True:
            solution+=str(i)+","

    return solution[:len(solution)-1]





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
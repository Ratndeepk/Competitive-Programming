
# You may change this function parameters
from collections import defaultdict
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
    n = numOfBankers
    p = numOfParticipants 
    bank = bankersPreferences
    boys = participantsPreferences
    bank_dic=defaultdict(list)
    boys_dic=defaultdict(list)
    #print(bank)
    #print(boys)
    count=1
    for i in bank:
        for j in range(len(i)):
            if count not in bank_dic:
                bank_dic[count]=[i[j]]
            else:
                bank_dic[count].append(i[j])
        count+=1 
    count=1
    for i in boys:
        for j in range(len(i)):
            if count not in boys_dic:
                boys_dic[count]=[i[j]]
            else:
                boys_dic[count].append(i[j])
        count+=1 
    print(bank_dic)
    print(boys_dic)
    if p>n:
        big = p 
        big_dic = boys_dic.copy() 
        small_dic = bank_dic.copy()
        small=n 
    else: 
        big=n 
        small_dic = boys_dic.copy() 
        big_dic = bank_dic.copy()
        small=p
    
    ans = [0]*small 
    matrix = [[False for i in range(small)] for i in range(big)]
    for i in range(big):
        for j in range(small):
            if j+1 in big_dic[i+1] or i+1 in small_dic[j+1]:
                matrix[i][j]=True 
                ans[j]+=1 
    #print(ans)
    for i in matrix:
        print(*i)
    return max(ans)

    

def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()



    
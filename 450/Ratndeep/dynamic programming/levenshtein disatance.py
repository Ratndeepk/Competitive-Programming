"""
Dynamic Programming 

Minimum Modification required to reach from one string to another
Levenshtein Distance Problem 
https://www.youtube.com/watch?v=MiqoA-yF-0M&t=58s&ab_channel=BackToBackSWE

Solving subproblems -> 

|  replace  |  insert   |
|  delete   | (current) | 

"""


def levenshtein(str1,str2):
    edit = [[0 for i in range(len(str1)+1)]for i in range(len(str2)+1)]

    for i in range(len(str1)+1):
        edit[i][0]=i 

    for i in range(len(str2)+1):
        edit[0][i]=i 

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]: 
                edit[i][j]=edit[i-1][j-1] # if characters are same treat them as they never existed
            else:
                edit[i][j] =  min(edit[i-1][j],edit[i][j-1],edit[i-1][j-1])+1  # otherwise taking minimum of Delete, Replace, Insert and adding 1 to it :) 

    return edit[len(str1)][len(str2)] 

    
    
    
str1 = input() 
str2 = input()

print(levenshtein(str1,str2))
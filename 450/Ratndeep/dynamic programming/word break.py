def wordbreakUtil(string,words,n,result):
    
    for i in range(1,n+1):
        prefix = string[:i]
        if prefix in words:
            if i==n:
                result+=prefix 
                print(result) 
                return 
            wordbreakUtil(string[i:],words,n-i,result+prefix+" ")




def wordbreak(string,words):
    n = len(string) 

    wordbreakUtil(string,words,n,"")



for _ in range(int(input())):
    string = input() 
    words = input().split() 

    wordbreak(string,words)
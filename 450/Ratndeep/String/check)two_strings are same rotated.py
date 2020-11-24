def check(str1,str2):
    if len(str1)!=len(str2):
        return False
        
    comb = str1+str2
    if comb.count(str1)>0:
        return True
    return False
str1 = input() 
str2 = input() 

print(check(str1,str2))
def check(str1,str2,combine):
    index=0
    for i in range(len(combine)):
        if index==len(str1):
            break
        if str1[index]==combine[i]:
            index+=1 

    if index!=len(str1):
        return False 

    index=0
    for i in range(len(combine)):
        if index==len(str2):
            break
        if str2[index]==combine[i]:
            index+=1 

    if index!=len(str2):
        return False 

    return True

str1 = input() 
str2 = input() 
combine = input() 
print(check(str1,str2,combine))


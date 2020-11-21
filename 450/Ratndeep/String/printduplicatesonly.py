str = input() 

dic={}
for i in str:
    if i in dic:
        dic[i]+=1 
    else:
        dic[i]=1 

for i,j in dic.items():
    if j>1:
        print(i,end=" ")
print() 
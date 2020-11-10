import math
def encryption(s):
    row = math.floor(math.sqrt(len(s)))
    col = math.ceil(math.sqrt(len(s)))
    if row*col==len(s):
        pass 
    elif row*col<len(s):
        row=col 
    elif row*col>len(s):
        if row*row>=len(s):
            col=row 
    #
    # print(row,col)
    matrix=[[None for i in range(col)]for i in range(row)]
    index=0
    for i in range(row):
        for j in range(col):
            try:
                matrix[i][j]=s[index]
                index+=1
            except IndexError:
                break
    final_ans=""
    for i in range(col):
        for j in range(row):
            if matrix[j][i]==None:
                break
            final_ans+=matrix[j][i]
        final_ans+=" "
    print(final_ans[:len(final_ans)-1])





string = input()
final_string="".join(string.split())
encryption(final_string)
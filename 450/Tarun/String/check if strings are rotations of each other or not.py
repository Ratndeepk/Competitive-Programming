#A Program to check if strings are rotations of each other or not
def solve(a,b):
    if len(a) != len(b):
        return False
    S = a + a
    if b in S:
        return True
    return False
    
a = 'abcde'
b = 'deabc'
solve(a,b)
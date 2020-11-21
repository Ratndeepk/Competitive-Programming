def multiplyTwoList(head1, head2):
    # Code here
    a=""
    b=""
    temp1=head1
    while temp1!=None:
        a+=str(temp1.data)
        temp1=temp1.next
    # print a
    temp2=head2
    while temp2!=None:
        b+=str(temp2.data)
        temp2=temp2.next
    # print b
    return (int(a)*int(b))%MOD

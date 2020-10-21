def reverse(head):
    prev = None
    current = head
    next = None
    
    while current is not None:
        next = current.next      
        current.next = prev       
        prev = current            
        current = next            
    
    return prev

def addLists(first, second):
    first = reverse(first)       
    second = reverse(second)     
    
    sumList = None
    carry = 0
    
    while first is not None or second is not None or carry>0:
        newVal = carry
        if first is not None:
            newVal += first.data
        if second is not None:
            newVal += second.data
  
        carry = newVal//10        
        newVal = newVal%10        
        
        newNode = Node(newVal)
        newNode.next = sumList
        sumList = newNode
        
        if first:
            first = first.next     
        if second:
            second= second.next
    
    return sumList

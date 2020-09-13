def reverse(head, k):
    current = head
    next = None
    prev = None
    count = 0
    
    while (current is not None and count < k):
        # reversing k elements
        next = current.next              # storing value of next node
        current.next = prev              # reversing link
        prev = current                   # updating prev
        current = next                   # updating current
        count += 1
    
    if next is not None:    # checking if there are more nodes ahead
        head.next = reverse(next, k)     # reversing those recursively
    
    return prev

def detectCycle(self, head: ListNode) -> ListNode:
    slow=head
    fast=head
    while slow:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    return slow.next

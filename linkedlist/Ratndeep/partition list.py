class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head=ListNode()
        after_head=ListNode()
        before=before_head
        after=after_head
        while(head):
            if head.val>=x:
                new_node=ListNode(head.val)
                after.next=new_node
                after=new_node
            elif head.val<x:
                new_node=ListNode(head.val)
                before.next=new_node
                before=new_node
            head=head.next
        before.next=after_head.next
        return before_head.next

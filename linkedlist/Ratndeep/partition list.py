class Solution:
    def put(self,node,head):
        temp=head
        if temp.val>=node.val:
            node.next=head
            head=node
        else:
            while(node.val>temp.next.val):
                temp=temp.next
            node.next=temp.next
            temp.next=node
        
        return node.next
        
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp=head
        while(temp.val!=x):
            temp=temp.next
        temp2=temp
        if temp.next:
            temp3=temp.next
        
            while(temp3):
                if temp3.val<=temp.val:
                    temp2.next=temp3.next
                    self.put(temp3,head)
                temp2=temp.next
                temp3=temp3.next
            return head
                    
        else:
            return head
        

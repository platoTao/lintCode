# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        L=head

        if head==None:
            return head
            
        else:
            next_node=head

            while(next_node.val==val):
                next_node=next_node.next
                L=next_node
                if L==None:
                    return None

            while(next_node.next!=None):
                if next_node.next.val==val:
                    if next_node.next.next!=None:
                        next_node.next=next_node.next.next
                    else:
                        next_node.next=None
                else:
                    next_node=next_node.next

        return L
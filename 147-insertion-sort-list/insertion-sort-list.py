# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        x = head
        
        while x:
            y = d
            
            while y.next and y.next.val < x.val:
                y = y.next
            
            z = x.next
            x.next = y.next
            y.next = x
            x = z
        
        return d.next
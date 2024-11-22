# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(head):
        res = ListNode()
        res.next = head
        pre = res
        curr = head
        
        while curr:
            # condition for duplicates
            while curr.next and curr.next.val == curr.val:
                # keep moving forward until curr.val != curr.next.val
                curr = curr.next
            
            # curr is still the node after curr
            # curr hasn't moved -> No duplicates detected, move pre forward
            if pre.next is curr:
                pre = pre.next
                
            # curr isn't the node next to pre
            # keep pre where it's now and skip all the nodes from pre to curr
            # because these are repeated values.
            else:
                pre.next = curr.next
            
            curr = curr.next
            
        return res.next
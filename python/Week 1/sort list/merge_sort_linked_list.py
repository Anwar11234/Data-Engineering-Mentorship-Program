class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if head is None or head.next is None:
        return head

    mid = findMiddleNode(head)
    midNext = mid.next
    mid.next = None
    list1 = sortList(head)
    list2 = sortList(midNext)
    return merge(list1, list2)

def findMiddleNode(head):
    prev = ListNode()
    prev.next = head
    slow = prev
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(list1, list2):
    res = ListNode()

    curr1 = list1
    curr2 = list2
    currRes = res

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            currRes.next = curr1
            curr1 = curr1.next
            currRes = currRes.next
        else:
            currRes.next = curr2
            curr2 = curr2.next
            currRes = currRes.next
    while curr1:
        currRes.next = curr1
        curr1 = curr1.next
        currRes = currRes.next

    while curr2:
        currRes.next = curr2
        curr2 = curr2.next
        currRes = currRes.next

    return res.next
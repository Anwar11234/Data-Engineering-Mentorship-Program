Problem Link: https://leetcode.com/problems/sort-list/

## Solution

I solved by using merge sort algorithm to sort the linked list, the merge sort algorithm has 3 main steps:

1. split the list into 2 havles, left half and right half.
2. recursively sort left and right halves.
3. merge the 2 sorted lists into 1 sorted list.

To apply these steps on linked lists, we need to get the middle node which is the node used to split the list into 2 halves, to get the middle of a linked list I used the fast and slow 2 pointers technique as follows:

```
def findMiddleNode(head):
    prev = ListNode()
    prev.next = head
    slow = prev
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

The next step is to split the linked list into 2 separate lists, the left half will be from the head of the linked list to the middle node, the right half will be from the node after the middle node to the end of the linked list. To physically separate the 2 halves we set the `next` pointer of the middle node to `None`. After splitting, we recursively sort the 2 halves and then merge them. The base case for the recursion will be a linked list with one node or an empty linked list and in that case we return the linked list as it's. Here's the code for splitting and recursively sorting the 2 havles:

```
def sortList(head):
    if head is None or head.next is None:
        return head

    mid = findMiddleNode(head)
    midNext = mid.next
    mid.next = None
    list1 = sortList(head)
    list2 = sortList(midNext)
    return merge(list1, list2)
```

The final step is the merge function, which is quite similar to the merging 2 sorted arrays:
```
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
```
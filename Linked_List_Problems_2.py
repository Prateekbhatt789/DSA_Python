from LinkedList_Basics import ListNode,printLL,Insert_At_Head
from typing import Optional


def kReverse_Recursive(head: ListNode, k: int):
    '''Reverse the list of k size batch'''
    # base case
    if not head:
        return head
    # recursive case
    # 1. Reverse the first k group
    prev, curr = None, head
    i = 0
    while curr and i < k:
        temp = curr.next 
        curr.next = prev
        prev = curr
        curr = temp
        i += 1
    
    # 2. Merge the k reversed list with rest of reversed list
    RevHeadFromFriend = kReverse_Recursive(curr,k)
    head.next = RevHeadFromFriend
    return prev


list = None
list = Insert_At_Head(list,6)
list = Insert_At_Head(list,5)
list = Insert_At_Head(list,4)
list = Insert_At_Head(list,3)
list = Insert_At_Head(list,2)
list = Insert_At_Head(list,1)
printLL(list,"List:")

list = kReverse_Recursive(list,3)
printLL(list,"List:")
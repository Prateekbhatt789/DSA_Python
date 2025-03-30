# LeetCode 21: Merge Two Sorted List
from typing import Optional
class ListNode:
    def __init__(self, val = 0 , next= None):
        self.val=val 
        self.next = next

def InsertAtHead(val: int, head: Optional[ListNode])-> Optional[ListNode]:
    temp = ListNode(val)
    temp.next = head
    return temp

def printLL(head: Optional[ListNode]):
    while head:
        print(f"{head.val}",end= " ")
        head = head.next
    print()

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode(0)
    temp = dummyHead
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    temp.next = list1 if list1 else list2
    return dummyHead.next


list1 = ListNode(4)
list1 = InsertAtHead(2, list1)
list1 = InsertAtHead(1, list1)
print("List1:",end=" ")
printLL(list1)

list2 = ListNode(4)
list2 = InsertAtHead(3, list2)
list2 = InsertAtHead(1, list2)
print("List2:",end=" ")
printLL(list2)

print("Merged List:",end=" ")
mergeHead = mergeTwoLists(list1=list1,list2=list2)
printLL(mergeHead)
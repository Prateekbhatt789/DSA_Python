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

# Optimised , No call stack overhead
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



def MergeLL(list1: ListNode,list2: ListNode) -> ListNode:
    ''' Recursive function to merge two sorted listed '''
    # Base Case
    if not list1:
        return list2
    if not list2:
        return list1
    # Recursive Case
    if list1.val <= list2.val:
        mergedLLHead = MergeLL(list1.next, list2)
        list1.next = mergedLLHead
        return list1
    else:
        mergedLLHead = MergeLL(list1, list2.next)
        list2.next = mergedLLHead
        return list2

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

print("Merged List using recursive function:",end=" ")
mergeHead = mergeTwoLists(list1=list1,list2=list2)
printLL(mergeHead)


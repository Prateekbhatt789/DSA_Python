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
    '''
    Merge two sorted linked lists 

    Time Complexisty: O(m+n)  ~O(n)
    Space Complexity: O(1)
    
    :param l1: The head of first Linked List
    :type l1: ListNode
    :param l2: The head of second Linked List
    :type l2: ListNode
    :return: The head of sorted Linked List
    :rtype: ListNode

    Time Complexity: O(n+m)
    Space Complexity: O(1)
    '''
    dummy = ListNode(0)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next



def MergeLL(list1: ListNode,list2: ListNode) -> ListNode:
    '''
    Docstring for merge_list_rec
    
    :param l1: The head of LL 1
    :type l1: ListNode
    :param l2: The head of LL 2
    :type l2: ListNode
    :return: Head of merged list
    :rtype: ListNode

    Time Complexity- O(m+n)
    Space Complexity- O(m+n) '''
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


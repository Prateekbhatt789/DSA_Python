# LeetCode 141: Linked List Cycle
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

def makecycle(head:Optional[ListNode],pos):
    count = 0
    dst,temp = head,head

    while head:
        if count < pos:
            dst = dst.next
            count+=1
        temp = head
        head = head.next
    
    temp.next = dst
    # print(temp.val)
    # print(dst.val)

def hasCycle( head: Optional[ListNode]) -> bool:
    '''
    Detects cycle in linked list 
    Also know as Tortoise and Hare algorithm or Floyed cycle detection

    :param head: head node of LL

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    slow ,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



list1 = ListNode(4)
list1 = InsertAtHead(0, list1)
list1 = InsertAtHead(2, list1)
list1 = InsertAtHead(3, list1)
print("List1:",end=" ")
printLL(list1)

# do not call printLL after makeCycle
makecycle(list1,1)    
print(hasCycle(list1))
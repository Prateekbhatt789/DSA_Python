# LeetCode 2: Add two number
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = None
    carry = 0 
    while l1 and l2:
        digit = (l1.val + l2.val + carry) % 10
        head = InsertToTail(head,digit)
        carry = (l1.val + l2.val + carry) // 10
        l1 = l1.next
        l2 = l2.next
    while l1:
        digit = (l1.val + carry) % 10
        InsertToTail(head,digit)
        carry = (l1.val + carry) // 10
        l1 = l1.next
    while l2:
        digit = (l2.val + carry) % 10
        InsertToTail(head,digit)
        carry = (l2.val + carry) // 10
        l2 = l2.next
    if carry:
        InsertToTail(head,carry)
    return head

def GetTail(head:Optional[ListNode]):
    while head.next:
        head = head.next
    return head

def InsertToTail(head:Optional[ListNode],val:int):
    temp = ListNode(val)
    if not head:
        head = temp
        return head
    tail = GetTail(head)
    tail.next = temp
    return head
def InsertAtHead(val: int, head: Optional[ListNode])-> Optional[ListNode]:
    temp = ListNode(val)
    temp.next = head
    return temp

def printLL(head: Optional[ListNode]):
    while head:
        print(f"{head.val}",end= " ")
        head = head.next
    print()

# list1 = ListNode(3)
# list1 = InsertAtHead(4, list1)
# list1 = InsertAtHead(2, list1)
# print("List1:",end=" ")
# printLL(list1)

# list2 = ListNode(4)
# list2 = InsertAtHead(6, list2)
# list2 = InsertAtHead(5, list2)
# print("List2:",end=" ")
# printLL(list2)

# print("Sum list:",end=" ")
# head = addTwoNumbers(list1,list2)
# printLL(head)
list1 = ListNode(9)
list1 = InsertAtHead(9, list1)
list1 = InsertAtHead(9, list1)
list1 = InsertAtHead(9, list1)
list1 = InsertAtHead(9, list1)
list1 = InsertAtHead(9, list1)
list1 = InsertAtHead(9, list1)
print("List1:",end=" ")
printLL(list1)

list2 = ListNode(9)
list2 = InsertAtHead(9, list2)
list2 = InsertAtHead(9, list2)
list2 = InsertAtHead(9, list2)
print("List2:",end=" ")
printLL(list2)

print("Sum list:",end=" ")
head = addTwoNumbers(list1,list2)
printLL(head)


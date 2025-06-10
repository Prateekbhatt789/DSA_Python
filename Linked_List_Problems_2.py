from LinkedList_Basics import ListNode,printLL,Insert_At_Head,Find_len
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

def KthNodeFromLast(head:ListNode, k: int) -> ListNode:
    '''Returns the Kth node from last'''
    first = head
    while k:
        first = first.next
        k -= 1

    second = head
    while first:
        first = first.next
        second = second.next
    return second

def PalindromeCheck(head: ListNode):
    if not head:
        return False
    # 1. find the middle point
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head2 = slow.next
    slow.next = None
    
    # 2. reverse the second half
    prev,curr = None, head2
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head2 = prev

    # 3. Compare the head and head2
    while head2:
        if head.val != head2.val:
            return False
        head = head.next
        head2 = head2.next
    return True

# Merge Sort 
def get_middle_modified( head: ListNode):
    prev = None
    slow,fast = head,head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None
    return slow

def Merge_SortedList_LL(head1: ListNode, head2: ListNode):
    dummy = ListNode(0)
    curr = dummy
    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 if not head2 else head2
    return dummy.next

def MergeSortLL(head: ListNode):
    if not head or not head.next:
        return head
    # 1. Find middle node
    middle = get_middle_modified(head)
    left = head
    right = middle

    # 2. Recursively sort list
    sortedList1 = MergeSortLL(left)
    sortedList2 = MergeSortLL(right)

    # 3. Merge sorted List
    head = Merge_SortedList_LL(sortedList1,sortedList2)
    return head

def kRotate (head: ListNode,k: int):
    l = Find_len(head)
    if k % l == 0 or not head:
        return head
    k = k % l
    fast = head
    while k:
        fast = fast.next
        k -= 1
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next
    newHead = slow.next
    slow.next = None
    fast.next = head
    return newHead

def Add_Two_List (head1: ListNode, head2: ListNode):
    dummy = ListNode(0)
    sumList = dummy
    carry = 0
    while head1 or head2:
        sum = 0 
        if head1:
            sum += head1.val
            head1 = head1.next
        if head2:
            sum += head2.val
            head2 = head2.next
        
        sum += carry
        digit = sum % 10
        carry = sum // 10
        tempNode = ListNode(digit)
        sumList.next = tempNode
        sumList = sumList.next

    return dummy.next


list = None
list = Insert_At_Head(list,6)
list = Insert_At_Head(list,5)
list = Insert_At_Head(list,4)
list = Insert_At_Head(list,3)
list = Insert_At_Head(list,2)
list = Insert_At_Head(list,1)
printLL(list,"List:")

# list = kReverse_Recursive(list,3)
# printLL(list,"List:")

Kth_Node = KthNodeFromLast(list,4)
print(Kth_Node.val)

list2 = None
list2 = Insert_At_Head(list2,1)
list2 = Insert_At_Head(list2,2)
list2 = Insert_At_Head(list2,3)
list2 = Insert_At_Head(list2,3)
list2 = Insert_At_Head(list2,2)
list2 = Insert_At_Head(list2,1)
printLL(list2,"List2")
printLL(list,"list")
print(f'Is List2 Palindrome: {PalindromeCheck(list2)}')
print(f'Is List Palindrome: {PalindromeCheck(list)}')

list3 = None
list3 = Insert_At_Head(list3,3)
list3 = Insert_At_Head(list3,5)
list3 = Insert_At_Head(list3,1)
list3 = Insert_At_Head(list3,2)
list3 = Insert_At_Head(list3,4)
printLL(list3,"List to sort")
list3 = MergeSortLL(list3)
printLL(list3,"Merged List")

list3 = kRotate(list3,k=13)
printLL(list3,"Rotate List")

list4 = None   # 342
list4 = Insert_At_Head(list4, 3)
list4 = Insert_At_Head(list4, 4)
list4 = Insert_At_Head(list4, 2)

list5 = None   # 465
list5 = Insert_At_Head(list5, 4)
list5 = Insert_At_Head(list5, 6)
list5 = Insert_At_Head(list5, 5)
printLL(list4,"Add list1")
printLL(list5,"Add list2")
sumList = Add_Two_List(list4, list5)
printLL(sumList,"Sum of 2 list")

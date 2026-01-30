# 234 Palindrome linked list - true if palindrome else false

from linked_list_module import ListNode,insert_at_head,printLL,get_list
from typing import Optional

def reverse_list(head):
    '''
    Reverse thee List starting from provided node
    
    :param head: ListNode
    Time Complexity: O(n)
    Space Complexity = O(1)
    '''
    if not head:
        return head
    prev,curr = None,head
    while curr:
        successor = curr.next
        curr.next = prev
        prev = curr
        curr = successor
    return prev


def isPalindrome(head: Optional[ListNode]):
    '''Approach: find middle and reverse second half and compare the two list node by node
    Time Complexity: O(n)
    Space Complexity = O(1)
    '''
    if not head:
        return True
    # 1. Find the middle of linked list
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse the ll from middle
    reversed_ll = reverse_list(slow)
    # 3. Reference to restore later
    copy_second_half = reversed_ll
    # 4. palindrome check for reversed and original list
    while reversed_ll:
        if head.val != reversed_ll.val:
            return False
        head = head.next
        reversed_ll = reversed_ll.next
    
    reverse_list(copy_second_half)
    return True

def isPalindrome_1(head:ListNode):
    '''store list  element inside a list and compare the original and reversed list
    Time Complexity: O(n)
    Space Complexity = O(n)
    '''
    result = []
    curr = head
    while  curr:
        result.append(curr.val)
        curr = curr.next
    return result == result[::-1]

# Palindrome Linked List
head = ListNode(1)
head = insert_at_head(2,head)
head = insert_at_head(3,head)
head = insert_at_head(2,head)
head = insert_at_head(1,head)

printLL(head)
print(f"Palindrome Check:{isPalindrome_1(head)}")
print()

temp = get_list(6)
printLL(temp)
print("Palindrome Check:",isPalindrome_1(temp))

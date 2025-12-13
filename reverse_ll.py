# 206. Reverse Linked List
from linked_list_module import ListNode,printLL,insert_at_head

def reverse_list(head):
    '''
    Reverse the linked list
    Uses iterative method to reverse
    :param head: head node of LL

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    if not head:
        return head
    curr,prev = head,None
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

def reverse_list_rec(head):
    '''
    Docstring for reverse_list_rec
    
    :param head: Description

    Time Complexity: O(n)

    '''
    # base case
    if not head.next:
        return head 
    # recursive case
    rev_head = reverse_list_rec(head.next)
    # add head to tail of this rev_head list
    rev_tail = head.next
    rev_tail.next = head
    head.next = None

    return rev_head


list1 = ListNode(8)
list1 = insert_at_head(7,list1)
list1 = insert_at_head(6,list1)
list1 = insert_at_head(5,list1)
list1 = insert_at_head(4,list1)
list1 = insert_at_head(3,list1)
list1 = insert_at_head(2,list1)
list1 = insert_at_head(1,list1)
printLL(list1,'Original List')

# list1 = reverse_list(list1)
# printLL(list1,'Reversed list')

list2 = reverse_list_rec(list1)
printLL(list2,'Recursively Reversed list')
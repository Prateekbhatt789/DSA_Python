# 876. Middle of the Linked List
from linked_list_module import printLL,get_list

def middle_of_list(head):
    '''
    finds the middle of linked list
    
    :param head: head node of linked list

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
head = get_list(7)
printLL(head)
mid = middle_of_list(head)
print(mid.val)
# 19. Remove Nth Node From End of List
from linked_list_module import get_list,printLL,ListNode

def remove_nth_node(head, n):
    '''
    Removes nth node from list
    
    :param head: head node of list
    :param n: int

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    # Step 0: Create a dummy node that points to the head.
    # This simplifies removal of the head node or single-node list.
    dummy = ListNode(0)
    dummy.next = head
    h1, h2 = dummy, dummy

    # Step 1: Move h1 pointer n+1 steps ahead.
    # This creates a gap of n nodes between h1 and h2.
    # The "+1" accounts for the dummy node.
    for _ in range(n + 1):
        h1 = h1.next

    # Step 2: Move both h1 and h2 pointers together until h1 reaches the end.
    # Now h2 will point to the node just before the one we want to remove.
    while h1:
        h1 = h1.next
        h2 = h2.next

    # Step 3: Remove the nth node from the end.
    # h2.next is the target node; skip it by pointing to the next node.
    h2.next = h2.next.next

    # Step 4: Return the new head.
    # dummy.next handles the case when the original head is removed.
    return dummy.next

head = get_list(8)
printLL(head)
head = remove_nth_node(head,2)
printLL(head)
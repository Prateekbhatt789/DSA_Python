from typing import Optional
from linked_list_module import ListNode,printLL,insert_at_head


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    dummy = ListNode(-1)
    dummy.next = head
    prev,curr = dummy,head

    while curr and curr.next:
        successor = curr.next
        
        curr.next = successor.next
        successor.next = curr
        prev.next = successor
        prev,curr = curr,curr.next
    return dummy.next

head = ListNode(6)
head = insert_at_head(5,head)
head = insert_at_head(4,head)
head = insert_at_head(3,head)
head = insert_at_head(2,head)
head = insert_at_head(1,head)

printLL(head)
swapped_list = swapPairs(head)
printLL(swapped_list,"Swapped List")
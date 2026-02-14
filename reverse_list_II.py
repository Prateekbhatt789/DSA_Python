from linked_list_module import printLL,ListNode,insert_at_head
from typing import Optional

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head

        dummy = ListNode(-1,head)
        leftPrev ,curr = dummy,head
        # 1 move curr to left position node
        for _ in range(left-1):
            leftPrev = leftPrev.next
        curr = leftPrev.next
        prev = None
        # 2 Reverse the sublist between left,right
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev,curr = curr,next_node

        # 3. Connection setup from linked list
        rev_tail = leftPrev.next
        rev_tail.next = curr
        leftPrev.next = prev
        return dummy.next

head = ListNode(5)
head = insert_at_head(4,head)
head = insert_at_head(3,head)
head = insert_at_head(2,head)
head = insert_at_head(1,head)

printLL(head)
head = reverseBetween(head,2,4)
printLL(head)
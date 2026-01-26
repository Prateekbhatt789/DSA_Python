#61 Rotate list

from linked_list_module import printLL,ListNode,get_list

def length_ll(head: ListNode)->int:
    k = 0
    while head:
        head = head.next
        k += 1
    return k

def rotate_right(head:ListNode,k:int):
    if not head:
            return head
    
    n = length_ll(head)

    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head
    
    new_tail = head
    for _ in range(n-k%n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head   

head = get_list(5)
printLL(head)
head = rotate_right(head,2)
printLL(head,"rotated list")
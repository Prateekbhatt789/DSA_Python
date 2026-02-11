from linked_list_module import insert_at_head,ListNode,printLL

def partition_list(head, x):
    dummy_before = ListNode(0)
    dummy_after = ListNode(0)
    before, after = dummy_before, dummy_after
    
    curr = head
    while curr:
        next_node = curr.next   # store next
        curr.next = None        # detach node
        
        if curr.val < x:
            before.next = curr
            before = curr
        else:
            after.next = curr
            after = curr
        
        curr = next_node

    before.next = dummy_after.next
    return dummy_before.next


head = ListNode(2)
head = insert_at_head(5,head)
head = insert_at_head(2,head)
head = insert_at_head(3,head)
head = insert_at_head(4,head)
head = insert_at_head(1,head)

printLL(head)

list = partition_list(head,3)
printLL(list)
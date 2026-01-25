# 25 Reverse node in k-Group 
from linked_list_module import printLL,ListNode,get_list

def get_kth_node(head:ListNode,k:int):
    '''
    Docstring for get_kth_node
    
    :param head: head pointer to LL
    :type head: ListNode
    :param k: K size group
    :type k: int
    '''
    # This can handle even group having nodes
    while head and k > 0:
        head = head.next
        k -= 1
    return head
    

def reverse_node_k_group(head: ListNode, k: int) -> ListNode:
    if k == 1 or not head:
        return head
    
    dummy = ListNode(0,head)
    group_prev = dummy

    while True:
        kth_node = get_kth_node(group_prev,k)
        if not kth_node:
            break
        next_group_start = kth_node.next

        prev,curr = kth_node.next,group_prev.next
        while curr != next_group_start:
            successor = curr.next
            curr.next = prev
            prev = curr
            curr = successor
        
        group_tail = group_prev.next
        group_prev.next = kth_node
        group_prev = group_tail
    
    return dummy.next
    
def recursive_reverse_node_k_group(head,k):
    # base case
    if not head:
        return head
    # recursive case

    kth_node = head
    i = 1
    # check whether k size group of node exist
    while kth_node and i <k:
        kth_node = kth_node.next
        i+= 1
        if not kth_node:
            # no need to reverse the linked list
            return head

    prev,curr = None,head
    for _ in range(k):
        successor = curr.next
        curr.next = prev
        prev = curr
        curr = successor

    head.next = recursive_reverse_node_k_group(curr,k)

    return prev
    

head = get_list()
printLL(head,"Original List")
k = int(input("Enter K:"))
# rev_head = reverse_node_k_group(head,k)
rev_head = recursive_reverse_node_k_group(head,k)
printLL(rev_head,"Recursive k-reverse list")
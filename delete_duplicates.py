# 
from linked_list_module import ListNode,printLL,insert_at_head,create_list_from_pyList

def delete_duplicates(head:ListNode):
    if not head:
        return head
    dummy = ListNode(-1,head)
    prev,curr = dummy,head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr = curr.next
        if prev.next != curr:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return dummy.next


lst = [1,2,3,3,3,4,4,4,4,4,4,5]

head = create_list_from_pyList(lst)
printLL(head,"duplicated list")
head = delete_duplicates(head)
printLL(head,"cleaned list")
from typing import Optional

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

# Printing Linked List
def printLL(head: ListNode, listName = 'Linked List'):
    '''Function to print Linked List'''
    if not head:
        print(f"No Node in {listName}")
        return None
    print(f"{listName}: ",end='')
    while head:
        print(f"{head.val}", end = " -> " if head.next else '\n')
        head = head.next
    # print(head.val)

# insert at head
def Insert_At_Head(head: ListNode, val: int) -> ListNode:
    tempNode = ListNode(val)
    tempNode.next = head
    return tempNode


# insert at tail
def Get_Tail(head: ListNode):
    while head.next:
        head = head.next
    return head

def Insert_At_Tail(head: ListNode, val: int) -> ListNode:
    if not head:
        return Insert_At_Head(head,val)
    tempNode = ListNode(val)
    tailNode = Get_Tail(head)
    tailNode.next = tempNode
    return head

# delete at head
def Delete_At_Head(head:ListNode) -> ListNode:
    if not head:
        return head
    return head.next

# delete at tail
def Delete_At_Tail(head: ListNode) -> ListNode:
    if not head :
        return head
    if not head.next:
        return None
    tailNode = Get_Tail(head)
    current = head
    while  current.next != tailNode:
        current = current.next
    current.next = None
    return head

# insert at index
def Insert_At_Index(head: ListNode,val: int ,pos: int) -> ListNode:
    if not head or pos == 1:
        return Insert_At_Head(head,val)
    current_pos = 1
    current_node = head
    while current_node and current_pos <= pos-1:
        current_node = current_node.next
        current_pos += 1
    if not current_node:
        print("Position is out of bound")
        return head
    successor_node = current_node.next
    new_node = ListNode(val)
    current_node.next  = new_node
    new_node.next = successor_node
    return head

# delete at index
def Delete_At_Index(head: ListNode, pos: int):
    if not head or pos <= 1:
        return Delete_At_Head(head)
    prev, curr = head, head
    curr_pos = 1
    while curr and curr_pos < pos:
        curr_pos += 1
        prev = curr
        curr = curr.next
    if not curr:
        return head
    prev.next = curr.next
    return head

# LL search
def Search_node(head: ListNode, search: int) -> bool:
    while head:
        if head.val == search:
            return True
        head = head.next

    return False
    
# LL len
def Find_len(head: ListNode) -> int:
    len = 0 
    while head:
        head = head.next
        len += 1
    return len

if __name__ == '__main__':
    list = None
    # list = Insert_At_Head(list,4)
    list = Insert_At_Head(list,3)
    list = Insert_At_Head(list,2)
    list = Insert_At_Head(list,1)
    printLL(list,'Sample List')

    list = Insert_At_Tail(list,4)
    printLL(list, "Tail_Insertion")

    # list = Delete_At_Head(list)
    # printLL(list,'Delete at head')

    # list = Delete_At_Tail(list)
    # printLL(list)

    # list = Insert_At_Index(list,45,2)
    # printLL(list,'at index')

    # list = Delete_At_Index(list,7)
    # printLL(list,'del at index')

    # value = int(input("Enter the value of Search node:"))
    # print(f"Node of value {value} found in List" if Search_node(list,value) else "Node of {value} not found in List")

    print(f"Length of list: {Find_len(list)}")
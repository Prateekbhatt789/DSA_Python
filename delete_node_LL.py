# 237. Delete Node in a Linked List
##### delete node but head will not be given, a node will be given but that willl not be last node of list
from linked_list_module import get_list,printLL,ListNode

def delete_node(node):
    '''
    Delete node from list
    
    :param node: LIstNode
    :rtype: none/void
    '''
    successor = node.next
    node.val = successor.val
    node.next = successor.next

# head node is not give
head = get_list(7)
printLL(head)

# Adding node to be deleted
node = ListNode(78)
node.next = head
node2 = ListNode(53)
node2.next = node

printLL(node2)
delete_node(node)
printLL(node2)
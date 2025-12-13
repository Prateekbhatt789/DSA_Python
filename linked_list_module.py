class ListNode:  
    ''' Blue Print to create object for singly Linked List'''
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

def insert_at_head(val,head):
    '''
    Place new node in front of Linked List
    
    :param val: int
    :param head: ListNode Custom Class

    Time Complexity : O(1) 
    '''
    new_node = ListNode(val)
    new_node.next = head
    return new_node

def get_tail(head):
    ''' gets tail node of Linked list '''
    if not head:
        return head
    while head.next:
        head = head.next
    return head

def insert_at_tail(val,head):
    '''
    Docstring for insert_at_tail
    
    :param val: Int
    :param head: ListNode Custom_Class
    '''
    new_node = ListNode(val)
    if not head:
        return new_node
    tail_node = get_tail(head)
    tail_node.next = new_node
    return head

def printLL(head,listname = 'Linked List'):
    ''' Print Linked list here 
        Time Complexity : O(n) '''
    if not head:
        print('Linked List is empty')
        return 
    print(f'{listname}:',end=' ')
    while head.next:
        print(head.val,end = '->')
        head = head.next
    print(head.val)

def get_list(n=5):
    list1 = ListNode(n)
    while n>1:
        list1 = insert_at_head(n-1,list1)
        n -= 1
    return list1

if __name__ == '__main__':
    head = None
    head = insert_at_head(30,head)
    head = insert_at_head(20,head)
    head = insert_at_head(10,head)
    printLL(head)
    head =insert_at_tail(40,head)
    printLL(head)
    temp = get_list(6)
    printLL(temp,'from get list')
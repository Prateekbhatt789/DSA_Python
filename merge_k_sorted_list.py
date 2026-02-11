from typing import Optional
from linked_list_module import ListNode,printLL,insert_at_head

def helper(list1,list2):
    dummy = ListNode(-1)
    temp = dummy
    while list1 and list2:
        val1 = list1.val
        val2 = list2.val
        if val1<=val2:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        
        temp = temp.next 
    temp.next = list1 if not list2 else list2
    return dummy.next


def mergeKList(lists:list[Optional[ListNode]]):
    '''
    k = number of linked lists
    N = total number of nodes across all lists
    Time Complexity: (nlogk)
    Space Complexity: O(k) bcz of merged[]
    '''
    if not lists:
        return None
    while  len(lists)>1:
        merged = []
        for i in range(0,len(lists),2):
            # Divide: separating the list to find the two
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            # Conquer: conquer the two separated list (here merge sort them)
            merged.append(helper(l1,l2))
        lists = merged
    return lists[0]

def mergedKList_recursive(lists:Optional[ListNode]):
    '''
    n is len of lists
    k is level
    Time Complexity : O(nlog k)
    Space Complexity : O(log k)
    '''
    # Base case
    if not lists:
        return None
    # Recursive case
    return divide(lists,0,len(lists)-1)

def divide(lists,left,right):
    if left == right:
        return lists[left]
    mid = (left + right) // 2
    l1 = divide(lists,left,mid)
    l2 = divide(lists,mid+1,right)
    return helper(l1,l2)


# List1 
l1 =  ListNode(5)
l1 = insert_at_head(4,l1)
l1 = insert_at_head(1,l1)

# List2
l2 = ListNode(4)
l2 = insert_at_head(3,l2)
l2 = insert_at_head(1,l2)

# List3
l3 = ListNode(6)
l3 = insert_at_head(2,l3)

printLL(l1,"List1")
printLL(l2,"List2")
printLL(l3,"List3")

# head = mergeKList([l1,l2,l3])
head1 = mergedKList_recursive([l1,l2,l3])
printLL(head1,'Recursive list')


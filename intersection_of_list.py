# 160. Intersection of Two Linked Lists
from linked_list_module import ListNode,printLL,insert_at_head

# Creating intersecting LL
headA  = ListNode('a2')
headA = insert_at_head('a1',headA)

headB = ListNode('b3')
headB = insert_at_head('b2',headB)
headB = insert_at_head('b1',headB)

headC = ListNode('c3')
headC = insert_at_head('c2',headC)
headC = insert_at_head('c1',headC)

curr = headA
while curr.next:
    curr = curr.next
curr.next = headC

curr = headB
while curr.next:
    curr = curr.next
curr.next = headC

printLL(headA,"List1")
printLL(headB,"List2")

def intersection_of_list(headA,headB):
    if not headA or not headB:
        return None
    currA,currB = headA,headB
    while currA != currB:
        currA = currA.next if currA else headB
        currB = currB.next if currB else headA
    return currA

intersection_node = intersection_of_list(headA,headB)
print("Intersection of List1 and list2:",intersection_node.val)
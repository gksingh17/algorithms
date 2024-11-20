class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def reverse_list_iterative(head):
        prev = None
        cur = head

        while cur:
            next_node = cur.next  # save next node
            cur.next = prev # reverse link
            prev = cur # prev becomes cur
            cur = next_node

        return prev # new head
    
    def reverse_list_recursive(head):
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = reverse_list_recursive(head.next) 
            head.next.next = head
        head.next = None        
        return new_head
    
def print_linked_list(head):
    cur = head
    while cur:
        print(cur.value, end= "->")
        cur = cur.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3)))
print_linked_list(head)
reversed_head = reverse_list_iterative()
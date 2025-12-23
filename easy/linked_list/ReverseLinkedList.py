from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __print__(self):
        l = []
        while self != None:
            l.append(self.val)
            self = self.next
        return l


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    # ListNode(1) -> ListNode(2) -> ListNode(3)
    '''
    current = ListNode(1)
    
    next_node =  ListNode(2)
    ListNode(1) -> None
    previous = ListNode(1)
    current = ListNode(2)
    
    
    next_node = ListNode(3)
    ListNode(2) -> ListNode(1)
    previous = ListNode(2)
    current = ListNode(3)

    '''
    previous = None
    current = head
    next_node = None
    
    while current != None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    print(reverseList(list1).__print__())
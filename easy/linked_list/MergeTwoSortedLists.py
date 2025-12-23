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

def mergeTwoLists(list1: Optional[ListNode],
                  list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(4, None)))
    print(mergeTwoLists(list1, list2).__print__())
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store, n = [], 0
        current = head

        while current:
            store.append(current.val)
            n += 1
            current = current.next

        dummy = ListNode(-1)
        current = dummy
        for i in range(n - 1, -1, -1):
            current.next = ListNode(store[i])
            current = current.next

        return dummy.next

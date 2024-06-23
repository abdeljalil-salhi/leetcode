# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Euclidean algorithm
        def gcd(a, b):
            return a if not b else gcd(b, a % b)

        current = head
        while current.next:
            saved = current.next
            current.next = ListNode(gcd(current.val, saved.val), saved)
            current = current.next.next

        return head

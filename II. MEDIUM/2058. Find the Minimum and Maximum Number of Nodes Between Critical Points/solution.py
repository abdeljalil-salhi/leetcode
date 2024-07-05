# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        current = head
        ans = [float("inf"), float("inf")]
        critical = []
        i, n = 2, 0

        while current and current.next and current.next.next:
            if (
                current.val < current.next.val > current.next.next.val
                or current.val > current.next.val < current.next.next.val
            ):
                critical.append(i)
                n += 1
                if n >= 2:
                    ans[0] = min(ans[0], abs(i - critical[n - 2]))
                    ans[1] = abs(i - critical[0])

            i += 1
            current = current.next

        return [-1, -1] if n < 2 else ans

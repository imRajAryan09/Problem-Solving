from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

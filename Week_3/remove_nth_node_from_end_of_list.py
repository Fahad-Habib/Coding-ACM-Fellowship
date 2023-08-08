class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        if head.next is None:
            return None
        s = head
        while s:
            l += 1
            s = s.next
        if n == l:
            head = head.next
            return head
        i = 0
        s = head
        while i < (l - n - 1):
            s = s.next
            i += 1
        if s.next.next is None:
            s.next = None
        else:
            s.next = s.next.next
        return head

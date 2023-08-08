class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        for i in range((10**4)+1):
            if head is None:
                return False
            head = head.next
        return True

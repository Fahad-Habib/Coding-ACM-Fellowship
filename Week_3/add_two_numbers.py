class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        while l1:
            n1.append(l1.val)
            l1 = l1.next

        while l2:
            n2.append(l2.val)
            l2 = l2.next
        n3 = int("".join([str(i) for i in reversed(n1)])) + int("".join([str(i) for i in reversed(n2)]))
        l3 = ListNode(n3%10)
        nxt = l3
        for i in str(n3)[::-1][1:]:
            nxt.next = ListNode(int(i))
            nxt = nxt.next

        return l3

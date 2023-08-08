class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        s = head
        i = 0
        while list1 and list2:
            if i == 0:
                s.val = min(list1.val, list2.val)
                i += 1
                if list1.val < list2.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
                continue
            s.next = ListNode(min(list1.val, list2.val))
            s = s.next
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next
        if not list1 and list2:
            while list2:
                if i == 0:
                    s.val = list2.val
                    list2 = list2.next
                    i += 1
                    continue
                s.next = ListNode(list2.val)
                s = s.next
                list2 = list2.next
            return head
        elif not list2 and list1:
            while list1:
                if i == 0:
                    s.val = list1.val
                    list1 = list1.next
                    i += 1
                    continue
                s.next = ListNode(list1.val)
                s = s.next
                list1 = list1.next
            return head

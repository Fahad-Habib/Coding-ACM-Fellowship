class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.arrayToBST(nums)
 
    def arrayToBST(self, nums):
        if not nums:
            return None
    
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.arrayToBST(nums[:mid])
        root.right = self.arrayToBST(nums[mid+1:])
        return root

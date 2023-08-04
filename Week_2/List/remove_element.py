class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        maxima = max(nums) + 1
        k = len(nums)
        for i, v in enumerate(nums):
            if v == val:
                nums[i] = maxima
                k -= 1
        nums.sort()
        return k

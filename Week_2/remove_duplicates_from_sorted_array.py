class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, val in enumerate(sorted(set(nums))):
            nums[i] = val
        return len(set(nums))

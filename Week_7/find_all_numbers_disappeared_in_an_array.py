class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        missing = []
        for i in range(1, n+1):
            if i not in nums:
                missing.append(i)
        return missing

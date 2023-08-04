class Solution:
    def maxArea(self, height: List[int]) -> int:
        amount = 0
        i, j = 0, len(height)-1
        while i < j:
            if height[i] <= height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            amount = max(amount, area)
        return amount

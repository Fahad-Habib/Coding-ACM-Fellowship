class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        length = len(nums) - 1
        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, length
            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return triplets

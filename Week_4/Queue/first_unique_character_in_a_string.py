class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, j in enumerate(s):
            if i == 0:
                if j not in s[i+1:]:
                    return i
            else:
                if j not in s[i+1:] and j not in s[:i]:
                    return i
        return -1
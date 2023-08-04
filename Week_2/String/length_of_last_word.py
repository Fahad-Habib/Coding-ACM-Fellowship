class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i in s.strip()[::-1]:
            if i == ' ':
                return l
            l += 1
        return l

        # Alternat one line solution but slower
        # return len(s.split()[-1])

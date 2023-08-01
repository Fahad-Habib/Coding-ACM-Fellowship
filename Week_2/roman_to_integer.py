class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        i = -1
        while i > -len(s):
            value += vals[s[i]]
            if s[i] in "VX" and s[i-1] == 'I':
                value -= 1
                i -= 1
            elif s[i] in "LC" and s[i-1] == 'X':
                value -= 10
                i -= 1
            elif s[i] in "DM" and s[i-1] == 'C':
                value -= 100
                i -= 1
            i -= 1
        if i == -len(s):
            value += vals[s[i]]
        return value

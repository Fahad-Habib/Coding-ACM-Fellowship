class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = ''
        l = 0
        for i in s:
            if i.isalnum():
                updated += i.lower()
                l += 1
        inc = 0
        if l%2 != 0:
            inc += 1
        for i, j in zip(updated[:l//2][::-1], updated[l//2+inc:]):
            if i != j:
                return False
        return True

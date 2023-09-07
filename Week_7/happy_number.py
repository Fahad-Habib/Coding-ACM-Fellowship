class Solution:
    def isHappy(self, n: int) -> bool:
        table = {}
        while True:
            if n in table:
                return False
            table[n] = 0
            table[n] = sum([int(i)**2 for i in str(n)])
            n = sum([int(i)**2 for i in str(n)])
            if n == 1:
                return True

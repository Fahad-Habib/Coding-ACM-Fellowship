class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaceables = {}
        if len(set(s)) != len(set(t)):
            return False
        for i, j in zip(s, t):
            if i not in replaceables:
                replaceables[i] = j
            else:
                if replaceables[i] != j:
                    return False
        return True

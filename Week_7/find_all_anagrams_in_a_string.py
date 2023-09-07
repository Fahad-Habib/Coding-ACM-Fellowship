class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p = "".join(sorted(list(p)))
        indices = []
        for i in range(len(s)-n+1):
            if "".join(sorted(list(s[i:i+n]))) == p:
                indices.append(i)
        return indices

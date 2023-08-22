class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        stack = []
        visited = set()

        for i, j in enumerate(s):
            last_occ[j] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        return ''.join(stack)

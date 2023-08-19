class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == matches[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        path = path.split('/')
        while '' in path:
            path.remove('')
        for i in path:
            if i == '.':
                pass
            elif i == '..':
                if len(path_stack) > 0:
                    path_stack.pop()
            else:
                path_stack.append(i)
        return '/' + '/'.join(path_stack)

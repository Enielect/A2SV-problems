class Solution:
    def simplifyPath(self, path: str) -> str:
        cur_path = path.split('/')
        stack = []
        for loc in cur_path:
            if loc !='' and loc!='.':
                if loc == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(loc)
        return '/' + '/'.join(stack)

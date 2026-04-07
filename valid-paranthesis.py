class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ']': '[', ')': '('}
        stack = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if stack and pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

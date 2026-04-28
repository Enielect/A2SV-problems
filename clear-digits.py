class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if not ch.isdigit():
                stack.append(ch)
            elif stack and not stack[-1].isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

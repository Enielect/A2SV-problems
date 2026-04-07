class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for path in logs:
            if path != '../' and path != './':
                stack.append(path)
            else:
                if stack and path == '../':
                    stack.pop()
        return len(stack)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '/':
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]

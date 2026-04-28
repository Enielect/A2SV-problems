class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and ast * stack[-1] < 0 and abs(ast) > stack[-1]:
                stack.pop()

            if not stack:
                stack.append(ast)
            elif ast < 0 and stack[-1] == abs(ast):
                stack.pop()
            elif stack[-1] < 0 or stack[-1] * ast > 0:
                stack.append(ast)
        return stack

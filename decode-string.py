class Solution:
    def decodeString(self, s: str) -> str:
        self.r = 0
        return self.helper(s)

    def helper(self, s):
        num, cur = 0, ''
        while self.r < len(s):
            ele = s[self.r]
            if ele == '[':
                self.r +=1
                inner = self.helper(s)
                cur += inner * num
                num = 0
            elif ele.isdigit():
                num = num * 10 + int(ele)
                self.r +=1
            elif ele == ']':
                self.r +=1
                return cur
            else:
                cur += ele
                self.r +=1
        return cur

# I did a stack approach inititally
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        r = 0
        while r < len(s):
            ch = s[r]
            cur = ''
            if ch == ']':
                while stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()
                stack.append(cur * stack.pop())
            else:
                if ch.isdigit():
                    num = int(ch)
                    while s[r+1].isdigit():
                        num = (num * 10) + int(s[r+1])
                        r +=1
                    stack.append(num)
                else:
                    stack.append(ch)
            r +=1
        return ''.join(stack)

class MyCalendar:
# This can definitely be written in a better way
    def __init__(self):
        self.store = []

    def book(self, st: int, et: int) -> bool:
        s = self.store
        s.sort()
        l, r = 0, len(s)-1
        #print(s)
        while l<=r:
            m =(l+r)//2
            #print(s[m])
            if s[m][0]<et and st<s[m][1]:
                return False
            elif s[m][0] >= et:
                r = m - 1
            else:
                l = m + 1
        s.append([st, et])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

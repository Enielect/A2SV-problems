# initially attempted approach (this doesn't use queue). I think this should be the optimal appproach

class DataStream:
    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.streak =  0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.streak +=1
        else:
            self.streak = 0
        return self.streak >= self.k

# Following the requirement to use a queue
      class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.queue = deque()

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.queue.append(num)
        else:
            self.queue = deque()

        return len(self.queue) >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

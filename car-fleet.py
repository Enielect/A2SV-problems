class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [0, 3, 5, 8, 10] => [1, 3, 1, 4, 2]
        # [12, 3, 7, 1, 1]
        # we just need to keep track of a monotonic decreasing stack since any element
        # that starts at a position earlier than some car is restricted by the speed of the 
        # car ahead

        times = [(target - pos) / sp for pos, sp in sorted(zip(position, speed))]
        stack = []
        for time in times:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)

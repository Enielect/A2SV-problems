class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        min_operations = 0
        i = 0
        for i in range(len(seats)):
            min_operations += abs(seats[i] - students[i])
        return min_operations

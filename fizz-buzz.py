class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n

        for j in range(n):
            i = j + 1
            if i % 3 == 0 and i % 5 == 0:
                res[j] = "FizzBuzz"
            elif i % 3 == 0:
                res[j] = "Fizz"
            elif i % 5 == 0:
                res[j] = "Buzz"
            else:
                res[j] = str(i)

        return res

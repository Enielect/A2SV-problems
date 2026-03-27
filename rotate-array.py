class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        original = nums[:]
        for i in range(k):
            nums[i] = original[n - k + i] 
        for j in range(k, n):
            nums[j] = original[j - k]

# first thing that should come to your head when doing rotating an array should always be modulus
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        for j in range(n):
            nums[j] = rotated[j]
          
# learn swapping subarray
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

# leraned the required solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # reverse the whole array.
        # reverse the first k portions, and the final n - k portion as sell
        n = len(nums)
        k = k % n
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1
        reverse(0, n - 1) # reverse the entire array
        reverse(0, k - 1) # reverse the first k portions
        reverse(k, n - 1) # reverse the final n - k portions

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        cnt, up = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                up +=1
            cnt += up
        return cnt

# second solution (less optimal) # 02-04-2026
# [1,1,2,2,3] 
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # track the number of dinstinct elements so far
        nums.sort()
        mini, unique = min(nums), 1
        frq, res = Counter(nums), 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] and nums[i] != mini:
                res += (unique * frq[nums[i]])
                unique +=1
        return res

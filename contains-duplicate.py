class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}

        for num in nums:
            check[num] = check.get(num, 0) + 1
            if check[num] > 1:
                return True
        return False

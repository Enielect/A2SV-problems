class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        def helper(l, r, first, score):
            if l > r:
                return score >= total - score
            if first == 0:
                return helper(l + 1, r, 1, score + nums[l]) or helper(l, r - 1, 1, score + nums[r])
            return helper(l + 1, r, 0, score) and helper(l, r - 1, 0, score) # If person 1 can win in any
            # of the ways then based on "greed" person 1 will follow that path and thus person 0 loses
        return helper(0, len(nums) - 1, 0, 0)

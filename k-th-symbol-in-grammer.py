class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k):
            total = 2 ** (n - 1)
            if k == 1:
                return 0
            
            if k > total // 2:
               return 1 - helper(n-1, k - total // 2)
            else:
                return helper(n-1, k)
        return helper(n,k)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # I'm sorry I don't know how to reverse the string using recursion
        # The worst thing to do in this life is to give up completely (just a simple intuition
        # that I got was sufficient)
        def reverse(l, r):
            if l >= r:
                return 
            s[l], s[r] = s[r], s[l]
            reverse(l+1, r-1)
        reverse(0, len(s) - 1)

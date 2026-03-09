class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        is_negative = num < 0
        num = -num if is_negative else num
        sorted_num = sorted(list(str(num)), reverse=True) if is_negative else sorted(list(str(num)))
        # find the first non-zero digit
        ans, zc = [], 0
        for n in sorted_num:
            if n != "0":
                ans.append(n)
                ans.extend(["0"]*zc)
                ans.extend(sorted_num[zc+1:])
                break
            zc +=1
        final = int("".join(ans))
        return -final if is_negative else final

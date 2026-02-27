import sys
import heapq

if __name__ == "__main__":
    # input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        input()
        arr = list(map(int, input().split(' ')))
        res, seen, final = [], set(), []
        # I think that we should sort first and then perform the check
        for _ in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        # I need to remove duplicates
        for a in arr:
            if a not in seen:
                seen.add(a)
                res.append(a)
        
        for r in range(len(res) - 1):
            cur = res[r]
            if cur + 1 != res[r + 1]:
                final.append(cur)

        print("NO" if len(final) >= 1 else "YES")

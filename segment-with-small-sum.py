def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    l = 0
    range_sum = 0
    maxi = 0
    for r in range(n):
        range_sum += a[r]
        while range_sum > s:
            range_sum -= a[l]
            l +=1
        maxi = max(maxi, r - l + 1)
    print(maxi)

if __name__ == "__main__":
    solve()

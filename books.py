def solve():
    n, t = map(int, input().split())
    a = list(map(int, list(input().split())))
    
    l= 0
    count, total = 0, 0
    for r in range(n):
        total += a[r]
        while l <= r and total > t:
            total -= a[l]
            l +=1
        count = max(r - l + 1, count)
    print(count)
if __name__ == "__main__":
    # input = sys.stdin.readline
    solve()

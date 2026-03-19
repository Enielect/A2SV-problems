def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    res = []
    l = r = 0
    while l < n and r < m:
        if a[l] < b[r]:
            l +=1
        else:
            res.append(l)
            r +=1
    if r < m:
        res.extend([n] * (m - r))
   
    print(" ".join(map(str, res)))
            
if __name__ == "__main__":
# input = sys.stdin.readline
    solve()

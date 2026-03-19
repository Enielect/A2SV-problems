def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    res = []
    l = r = 0
    while l < n and r < m:
        if a[l] <= b[r]:
            res.append(a[l])
            l +=1
        else:
            res.append(b[r])
            r +=1
    if l < n:
        res.extend(a[l:n])
    if r < m:
        res.extend(b[r:m])
   
    print(" ".join(map(str, res)))
            
if __name__ == "__main__":
# input = sys.stdin.readline
    solve()

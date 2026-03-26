def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    alleven = all(x % 2 == 0 for x in a)
    allodd = all(x % 2 == 1 for x in a)
    
    if alleven or allodd:
        return a
    else:
        return sorted(a)

if __name__ == "__main__":
    res = solve()
    print(*res)

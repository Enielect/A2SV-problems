if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    
    a.sort()
    if k == 0:
        x = a[0] - 1
        print(x if x >= 1 else -1)
    elif k == n:
        print(a[-1])
    else:
        if a[k-1] == a[k]:
            print(-1)
        else:
            print(a[k-1])

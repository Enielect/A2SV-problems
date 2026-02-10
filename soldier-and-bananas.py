if __name__ == "__main__":
    k, n, w = map(int, input().split(' '))
    
    sum = k*(w * (w + 1) // 2)
    
    if sum - n > 0:
        print(sum - n)
    else:
        print(0)

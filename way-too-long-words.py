if __name__ == "__main__":
    t = int(input())
     
    for _ in range(t):
        w = input()
        n = len(w)
        if n > 10:
            print(f"{w[0]}{n-2}{w[-1]}")
        else:
            print(w)

if __name__ == "__main__":
    for j in range(5):
        row = input().split(' ')
        for i in range(len(row)):
            if row[i] == '1':
                print(abs(2 - i) + abs(2 - j))
                break

import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

dict = {key: val for key, val in [input().strip().split() for _ in range(n)]}

for line in sys.stdin:
    cur = line.strip()
    if cur in dict:
        print(f"{cur}={dict[cur]}")
    else: 
        print("Not found")

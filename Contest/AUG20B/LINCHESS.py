import sys

testcases = int(input())

for _ in range(0, testcases):
    n, k = list(map(int, input().split()))
    p = list(map(int, input().split()))

    mini = sys.maxsize
    index = -1
    
    for i in range(0, n):
        pi = p[i]
        if pi <= k:
            diff = abs(pi - k)
            if diff >= pi and diff % pi == 0:
                if diff // pi < mini:
                    mini = diff // pi
                    index = i
    
    
    print(-1 if index == -1 else p[index])

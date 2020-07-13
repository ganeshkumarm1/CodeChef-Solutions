from functools import reduce

testcases = int(input())

for t in range(testcases):
    n = int(input())
    vals = list(map(int, input().split()))
    missed = 0
    
    for i in range(1, len(vals)):
        x = abs(vals[i] - vals[i - 1])

        if x > 0:
            x -= 1
        
        missed += x
    
    print(missed)


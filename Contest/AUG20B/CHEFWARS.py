import math

testcases = int(input())

for _ in range(0, testcases):
    health, power = list(map(int, input().split()))

    ans = 0

    while power != 0:
        ans += power
        power = math.floor(power / 2)
    
    print(1 if ans >= health else 0)

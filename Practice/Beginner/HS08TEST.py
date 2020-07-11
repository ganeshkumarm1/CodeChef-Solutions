x, y = list(map(float, input().split()))

if x % 5 != 0 or x > y - 0.5:
    print(y)
else:
    print(y - x - 0.5)

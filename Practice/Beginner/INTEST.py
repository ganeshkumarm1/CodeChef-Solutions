n, k = list(map(int, input().split()))

result = 0
for i in range(n):
    x = int(input())
    result += 1 if x % k == 0 else 0

print(result)
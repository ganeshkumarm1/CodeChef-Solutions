n = int(input())

arr = list(map(int, input().split()))

maxi = -1

for i in arr:
    if i > maxi:
        maxi = i

first_max = maxi
maxi = -1

for i in arr:
    if i % first_max > maxi:
        maxi = i % first_max

print(maxi)
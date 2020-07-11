t = int(input())

for i in range(t):
    n = int(input())

    result = 0

    while n != 0:
        n, r = divmod(n, 10)
        result += r
    
    print(result)
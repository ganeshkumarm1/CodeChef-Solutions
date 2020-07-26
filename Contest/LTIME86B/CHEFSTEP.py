t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    ans = ""
    
    s = map(int, input().split())

    for c in s:
        d, r = divmod(c, k)

        if r == 0:
            ans += '1'
        else:
            ans += '0'
    
    print(ans)

t = int(input())

for i in range(t):
    n = int(input())

    occur = {
        'c': 0,
        'o': 0,
        'd': 0,
        'e': 0,
        'h': 0,
        'f': 0
    }

    for j in range(n):
        s = input()

        for c in s:
            if c in occur:
                occur[c] += 1

    
    ans = min([occur['o'], occur['d'], occur['h'], occur['f'], int(occur['c']/2), int(occur['e']/2)])
    print(ans)
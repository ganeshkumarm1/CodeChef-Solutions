t = int(input())

def solve(S, n):
    if len(S) == 1:
        if S[0] == 'cookie':
            return "NO"
        else:
            return "YES"

    ate_cookie = True if S[0] == 'cookie' else False

    for j in range(1, n):
        s = S[j]
        if ate_cookie:
            if s != 'milk':
                return "NO"
            else:
                ate_cookie = False

        if s == 'cookie':
            ate_cookie = True
    if ate_cookie:
        return "NO"
    
    return "YES"
    
for i in range(t):
    n = int(input())

    S = list(input().split())

    print(solve(S, n))

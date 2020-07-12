t = int(input())

def solve(m, w):
    if m == w:
        return "YES"
    
    a, b = (m, w) if len(m) > len(w) else (w, m)

    ai = 0
    bi = 0

    while ai < len(a) and bi < len(b):
        if a[ai] == b[bi]:
            ai += 1
            bi += 1
        else:
            ai += 1
    
    
    if bi == len(b):
        return "YES"
    else:
        return "NO"


for i in range(t):
    m, w = input().split()

    print(solve(m, w))
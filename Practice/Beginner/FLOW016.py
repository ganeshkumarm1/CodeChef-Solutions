t = int(input())

def find_gcd(a, b):
    if a % b == 0:
        return b
    
    return find_gcd(b, a % b)

def find_lcm(a, b, gcd):
    return int((a * b)/gcd)

for i in range(t):
    a, b = list(map(int, input().split()))
    gcd = find_gcd(a, b)
    lcm = find_lcm(a, b, gcd)
    print(gcd, lcm)
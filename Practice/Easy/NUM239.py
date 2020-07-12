t = int(input())

for i in range(t):
    l, r = list(map(int, input().split()))

    l_rem = l % 10
    l_round = l - l_rem

    r_rem = r % 10
    r_round = r - r_rem

    result = 0

    result += ((r_round - l_round) // 10) * 3

    
    if r_rem != 0:
        if r_rem >= 2:
            result += 1
        if r_rem >= 3:
            result += 1
        if r_rem >= 9:
            result += 1

    if l_rem != 0:
        if l_rem > 2:
            result -= 1
        if l_rem > 3:
            result -= 1
        if l_rem > 9:
            result -= 1
    
    print(result)
testcases = int(input())

def is_equal(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

for testcase in range(testcases):
    n = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    s1.sort()
    s2.sort()

    if(is_equal(s1, s2)):
        print("0")
        continue

    left_side = {}
    right_side = {}

    for i in range(len(s1)):
        num1 = s1[i]
        num2 = s2[i]

        if num1 in left_side:
            left_side[num1] += 1
        else:
            left_side[num1] = 1
        
        if num1 not in right_side:
            right_side[num1] = 0
        
        if num2 in right_side:
            right_side[num2] += 1
        else:
            right_side[num2] = 1
        
        if num2 not in left_side:
            left_side[num2] = 0
    
    swappable = True

    swappablesl = {}
    swappablesr = {}
    for key in left_side:
        if (left_side[key] + right_side[key]) % 2 == 1:
            swappable = False
            break
        else:
            m = left_side[key] if left_side[key] > right_side[key] else right_side[key]
            d = 'to_r' if left_side[key] > right_side[key] else 'to_l'
            swap_count = m - int((left_side[key] + right_side[key])/2)
            if d == 'to_r':
                swappablesl[key] = swap_count
            else:
                swappablesr[key] = swap_count
    
    if not swappable:
        print("-1")
        continue

    l = []
    r = []
    for key in swappablesl:
        l.extend([key] * swappablesl[key])
    for key in swappablesr:
        r.extend([key] * swappablesr[key])
    l.sort()
    r.sort(reverse=True)
    
    s = s1 + s2
    mini = min(s)
    
    min_cost = 0
    for i in range(len(l)):
        if min(l[i], r[i]) < mini * 2:
            min_cost = min_cost + min(l[i], r[i])
        else:
            min_cost = min_cost + (2 * mini)
    
    print(min_cost)
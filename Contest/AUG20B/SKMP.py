import string

t = int(input())

for _ in range(t):
    s = input()
    p = input()

    sd = {}
    pd = {}

    for c in s:
        if c not in sd:
            sd[c] = 1
        else:
            sd[c] += 1
    
    for c in p:
        if c not in pd:
            pd[c] = 1
        else:
            pd[c] += 1
    
    ans = ''

    for c in string.ascii_lowercase:
        if c in sd or c in pd:
            if c not in pd:
                ans += c * sd[c]
                sd[c] = 0
            else:
                diff = abs(sd[c] - pd[c])
                ans += c * diff
                sd[c] -= diff
            

    p0_in_ans = False

    for c in ans:
        if c == p[0]:
            p0_in_ans = True
            break
    
    if not p0_in_ans:
        index = -1
        for i in range(0, len(ans)):
            if p[0] < ans[i]:
                index = i
                break
                
        if index == -1:
            index = len(ans)

        print(ans[0: index] + p + ans[index: len(ans)])

    else:
        indexes = []
        for i in range(0, len(ans)):
            if ans[i] == p[0]:
                indexes.append(i)

        start, end = min(indexes), max(indexes)
        end += 1
        x = ans[0:start] + p + ans[start: len(ans)]        
        y = ans[0:end] + p + ans[end: len(ans)]
        
        print(min(x, y))
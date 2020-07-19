t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    dic = {}

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    is_yes = True
    for key in dic:
        if(dic[key] %  2 == 1):
            is_yes = False
            break

    if(is_yes):
        print("YES")
    else:
        print("NO")
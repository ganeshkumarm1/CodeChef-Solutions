from collections import OrderedDict

t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    
    dic = OrderedDict()
    for a in arr:
        if str(a) in dic:
            dic[str(a)] += 1
        else:
            dic[str(a)] = 1
    
    print(len(dic.keys()))


t = int(input())


for _ in range(t):
    n, k = list(map(int, input().split()))

    w = list(map(int, input().split()))

    s = sum(w)

    check = False
    for i in w:
        if i > k:
            check = True
    if check:
        print(-1)
        continue
    
    if s <= k:
        print(1)
    else:
        pos = -1
        s = 0
        cnt = 0
        i = 0
        st = []
        while i < n:
            x = w[i]
            s += x
            
            if s == k:
                cnt += 1
                st.append(i)
                s = 0
            elif s > k:
                i -= 1
                s = 0
                cnt += 1
                st.append(i)
                
            else:
                if i == n - 1:
                    st.append(i)
                   
            i += 1
            
        print(len(st))



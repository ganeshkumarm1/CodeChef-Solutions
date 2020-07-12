t = int(input())

for i in range(t):
    n = input().strip()

    lucky_digits = ['4', '7']

    non_lucky_count = 0

    for c in n:
        if c not in lucky_digits:
            non_lucky_count += 1
    
    print(non_lucky_count)
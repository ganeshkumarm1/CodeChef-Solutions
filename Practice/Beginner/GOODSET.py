t = int(input())

def print_result(r):
    print(" ".join(r))

for i in range(t):
    n = int(input())

    result = ['1', '2', '4']

    if n <= 3:
        print_result(result[0: n])
    else:
        start = 4
        for j in range(0, n - 3):
            start += 3
            result.append(str(start))
        
        print_result(result)
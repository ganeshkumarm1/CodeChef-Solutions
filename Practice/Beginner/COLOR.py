t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    counts = {
        'R': 0,
        'G': 0,
        'B': 0
    }

    for c in s:
        counts[c] += 1
        
    colors = [counts['R'], counts['G'], counts['B']]
    colors.sort()

    print(colors[0] + colors[1])
    
t = int(input())

def solve(brackets):
    stack = 0

    longest_prefix = 0

    for j in range(0, len(brackets)):
        bracket = brackets[j]
        if bracket == '<':
            stack += 1
        else:
            stack -= 1
        
        if stack == 0:
            longest_prefix = j + 1
        elif stack < 0:
            return longest_prefix
    
    return longest_prefix

for i in range(t):
    brackets = input()

    print(solve(brackets))
testcases = int(input())

for _ in range(0, testcases):
    pc, pr = list(map(int, input().split()))

    nnm_of_9_pc = pc if pc % 9 == 0 else pc + 9 - (pc % 9)
    nnm_of_9_pr = pr if pr % 9 == 0 else pr + 9 - (pr % 9)


    digits_pc = nnm_of_9_pc // 9
    digits_pr = nnm_of_9_pr // 9

    who_wins = '1' if digits_pc >= digits_pr else '0'
    min_digit = digits_pc if who_wins == '0' else digits_pr

    print(who_wins, min_digit)



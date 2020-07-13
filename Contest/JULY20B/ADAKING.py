testcases = int(input())

def print_board(board):
    for i in range(8):
        print("".join(board[i]))

for testcase in range(testcases):
    k = int(input())

    board = [['X'] * 8 for x in range(8)]

    start = (3, 3)

    dire = 'r'

    while k != 0:
        r, c = start

        if(r == 3 and c == 3):
            board[r][c] = 'O'
        else:
            board[r][c] = '.'
        
        if dire == 'r':
            if start not in [(3, 4), (2, 5), (1, 6), (0, 7)]:
                c += 1
            else:
                r += 1
                dire = 'd'
        elif dire == 'd':
            if start not in [(4, 4), (5, 5), (6, 6), (7, 7)]:
                r += 1
            else:
                c -= 1
                dire = 'l'
        elif dire == 'l':
            if start not in [(4, 2), (5, 1), (6, 0)]:
                c -= 1
            else:
                r -= 1
                dire = 'u'
        else:
            if start not in [(2, 2), (1, 1), (0, 0)]:
                r -= 1
            else:
                c += 1
                dire = 'r'
        
        start = (r, c)
        k -= 1

    print_board(board)
    



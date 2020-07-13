testcases = int(input())


def sort_pts_by_x_and_y(pts, axis):
    return sorted(pts, key=lambda pt: pt[axis])


for testcase in range(testcases):
    n = int(input())
    m = 4 * n

    pts = []

    for i in range(m - 1):
        x, y = list(map(int, input().split()))
        pts.append((x, y))

    pts_x_axis = sort_pts_by_x_and_y(pts, 1)
    pts_y_axis = sort_pts_by_x_and_y(pts, 0)

    problem_x = -1
    problem_y = -1

    row_pts = 1
    x1 = y1 = -1
    x2 = y2 = -1

    i = 0

    while i < len(pts_x_axis) - 1:
        x1, y1 = pts_x_axis[i]
        x2, y2 = pts_x_axis[i + 1]

        if y1 == y2:
            row_pts += 1
        else:
            if row_pts % 2 == 1:
                problem_x = y1
                break
            row_pts = 1

        i += 1

    if i == len(pts_x_axis) - 1:
        problem_x = y2

    col_pts = 1
    i = 0
    while i < len(pts_y_axis) - 1:
        x1, y1 = pts_y_axis[i]
        x2, y2 = pts_y_axis[i + 1]

        if x1 == x2:
            col_pts += 1
        else:
            if col_pts % 2 == 1:
                problem_y = x1
                break
            col_pts = 1

        i += 1

    if i == len(pts_y_axis) - 1:
        problem_y = x2
    print(str(problem_y) + " " + str(problem_x))

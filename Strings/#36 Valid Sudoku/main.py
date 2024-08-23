def solve(board):
    # All Rows
    for i in range(9):
        my = {}
        for j in range(9):
            item = board[i][j]
            if item == ".":
                continue
            elif item in my:
                return False
            else:
                my[item] = j

    # All Columns
    for i in range(9):
        my = {}
        for j in range(9):
            item = board[j][i]
            if item == ".":
                continue
            elif item in my:
                return False
            else:
                my[item] = j
    # All Boxes
    for i_start in range(0, 9, 3):
        for j_start in range(0, 9, 3):
            my = {}
            for i in range(i_start, i_start + 3):
                for j in range(j_start, j_start + 3):
                    item = board[i][j]
                    if item == ".":
                        continue
                    elif item in my:
                        return False
                    else:
                        my[item] = j
    return True


print(
    solve(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    solve(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

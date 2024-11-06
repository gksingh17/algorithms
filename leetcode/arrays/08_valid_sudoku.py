from collections import defaultdict


def valid_sudoku(board: list(list([str]))) -> bool:
    # {0 : ( 5, 3, 7),
    # 1 : (6 1 9 5 ) rows
    rows = defaultdict(set)  # row set to check for duplicates
    cols = defaultdict(set)
    squares = defaultdict(set)  # key r // 3, c //3 checks each sub square
    # (0, 1) (0, 2) (1, 0), (1, 1) ...

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    print(squares)
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
        ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


print(valid_sudoku(board))

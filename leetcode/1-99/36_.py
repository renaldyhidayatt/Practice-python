from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    for i in range(9):
        tmp_row = [0] * 10
        tmp_col = [0] * 10
        for j in range(9):
            # Check row
            cell_val_row = board[i][j]
            if cell_val_row != ".":
                index_row = int(cell_val_row)
                if index_row > 9 or index_row < 1:
                    return False
                if tmp_row[index_row] == 1:
                    return False
                tmp_row[index_row] = 1

            # Check column
            cell_val_col = board[j][i]
            if cell_val_col != ".":
                index_col = int(cell_val_col)
                if index_col > 9 or index_col < 1:
                    return False
                if tmp_col[index_col] == 1:
                    return False
                tmp_col[index_col] = 1

    for i in range(3):
        for j in range(3):
            tmp = [0] * 10
            for ii in range(i * 3, i * 3 + 3):
                for jj in range(j * 3, j * 3 + 3):
                    cell_val = board[ii][jj]
                    if cell_val != ".":
                        index = int(cell_val)
                        if tmp[index] == 1:
                            return False
                        tmp[index] = 1
    return True

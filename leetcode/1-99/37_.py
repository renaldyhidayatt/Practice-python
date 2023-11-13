from typing import List


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def solve_sudoku(board: List[List[str]]) -> None:
    pos = []
    find = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                pos.append(Position(x=i, y=j))
    put_sudoku(board, pos, 0, find)


def put_sudoku(
    board: List[List[str]], pos: List[Position], index: int, succ: bool
) -> None:
    if succ:
        return
    if index == len(pos):
        succ = True
        return
    for i in range(1, 10):
        if check_sudoku(board, pos[index], i, pos):
            if not succ:
                board[pos[index].x][pos[index].y] = str(i)
                put_sudoku(board, pos, index + 1, succ)
                if succ:
                    return
                board[pos[index].x][pos[index].y] = "."


def check_sudoku(
    board: List[List[str]], pos: Position, val: int, positions: List[Position]
) -> bool:
    for i in range(len(board[0])):
        if board[pos.x][i] != "." and int(board[pos.x][i]) == val:
            return False

    for i in range(len(board)):
        if board[i][pos.y] != "." and int(board[i][pos.y]) == val:
            return False

    pos_x, pos_y = pos.x - pos.x % 3, pos.y - pos.y % 3
    for i in range(pos_x, pos_x + 3):
        for j in range(pos_y, pos_y + 3):
            if board[i][j] != "." and int(board[i][j]) == val:
                return False

    return True

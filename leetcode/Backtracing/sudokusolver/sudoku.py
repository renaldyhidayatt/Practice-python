from typing import List


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def solveSudoku(board: List[List[str]]) -> None:
    pos, find = [], False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                pos.append(Position(x=i, y=j))
    putSudoku(board, pos, 0, find)


def putSudoku(
    board: List[List[str]], pos: List[Position], index: int, succ: bool
) -> None:
    if succ:
        return
    if index == len(pos):
        succ = True
        return
    for i in range(1, 10):
        if checkSudoku(board, pos[index], i) and not succ:
            board[pos[index].x][pos[index].y] = str(i)
            putSudoku(board, pos, index + 1, succ)
            if succ:
                return
            board[pos[index].x][pos[index].y] = "."


def checkSudoku(board: List[List[str]], pos: Position, val: int) -> bool:
    for i in range(len(board[0])):
        if board[pos.x][i] != "." and int(board[pos.x][i]) == val:
            return False
    for i in range(len(board)):
        if board[i][pos.y] != "." and int(board[i][pos.y]) == val:
            return False
    posx, posy = pos.x - pos.x % 3, pos.y - pos.y % 3
    for i in range(posx, posx + 3):
        for j in range(posy, posy + 3):
            if board[i][j] != "." and int(board[i][j]) == val:
                return False
    return True

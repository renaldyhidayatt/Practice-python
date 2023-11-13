dir = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]


def exist(board, word):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if search_word(board, visited, word, 0, i, j):
                return True
    return False


def is_in_board(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])


def search_word(board, visited, word, index, x, y):
    if index == len(word) - 1:
        return board[x][y] == word[index]

    if board[x][y] == word[index]:
        visited[x][y] = True
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if (
                is_in_board(board, nx, ny)
                and not visited[nx][ny]
                and search_word(board, visited, word, index + 1, nx, ny)
            ):
                return True
        visited[x][y] = False

    return False

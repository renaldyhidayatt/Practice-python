def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    matrix = [[] for _ in range(numRows)]
    down, up = 0, numRows - 2

    for i in range(len(s)):
        if down != numRows:
            matrix[down].append(s[i])

            down += 1

        elif up > 0:
            matrix[up].append(s[i])
            up -= 1

        else:
            up = numRows - 2
            down = 0

    solution = ""

    for row in matrix:
        solution += "".join(row)

    return solution


print(convert("PAYPALISHIRING", 4))

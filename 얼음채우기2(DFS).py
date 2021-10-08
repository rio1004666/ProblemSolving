def dfs(y, x):
    if n > y + 1 >= 0 and m > x >= 0 and board[y + 1][x] == 0:
        board[y + 1][x] = 1
        dfs(y + 1, x)
    if n > y - 1 >= 0 and m > x >= 0 and board[y - 1][x] == 0:
        board[y - 1][x] = 1
        dfs(y - 1, x)
    if n > y >= 0 and m > x + 1 >= 0 and board[y][x + 1] == 0:
        board[y][x + 1] = 1
        dfs(y, x + 1)
    if n > y >= 0 and m > x - 1 >= 0 and board[y][x - 1] == 0:
        board[y][x - 1] = 1
        dfs(y, x - 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                continue
            else:
                result += 1
                dfs(i, j)
                print(board)
    print(result)

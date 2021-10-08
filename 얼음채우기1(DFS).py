def dfs(y, x):
    for dy, dx in dxy:
        ny = y + dy
        nx = x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= m or board[ny][nx] == 1:
            continue
        board[ny][nx] = 1
        dfs(ny, nx)


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    result = 0
    # print(board)
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 4방향 탐색
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                continue
            else:
                result += 1
                dfs(i, j)
                # print(board)
    print(result)
    # print(board)

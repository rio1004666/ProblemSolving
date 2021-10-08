def dfs(y, x):
    if y < 0 or x < 0 or y >= n or x >= m:  #인덱스에 이미 마이너스가 들어가버린다.
        return
    if board[y][x] == 0:
        board[y][x] = 1
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
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
    print(result)

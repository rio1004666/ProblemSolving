from collections import deque


def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        crx, cry, cbx, cby, depth = queue.popleft()
        # 꺼냇는데 움직인 횟수가 10번 초과했다면 이제 반복문을 빠져나올것이다
        # 첫번째 10번째 초과는 무조건 뒤로도 10번 초과했을 것이므로 더이상 체킹하지 않는다.
        if depth > 10:
            break
        for dx, dy in dxy:
            # 4가지 방향으로 각각 이동해본다
            nrx, nry, rcnt = move(crx, cry, dx, dy)
            nbx, nby, bcnt = move(cbx, cby, dx, dy)
            # 그 위치결과와 움직인 횟수가 나온다 이제 파란구슬과 빨간구슬 게임판정이 들어간다.
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return depth  # 게임이 끝나는 경우 바로 움직인 횟수를 반환한다 각 4가지 방향은 같은 움직인 횟수이다.
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1


if __name__ == '__main__':
    row, col = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(row)]
    visited = [[[[False] * col for _ in range(row)] for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx, ry = i, j
            if board[i][j] == 'B':
                bx, by = i, j
    print(bfs(rx, ry, bx, by))

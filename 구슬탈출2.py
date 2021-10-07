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
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for dx, dy in dxy:
            new_rx, new_ry, rcnt = move(rx, ry, dx, dy)
            new_bx, new_by, bcnt = move(bx, by, dx, dy)
            if board[new_bx][new_by] != 'O':  # 전제 조건은 블루는 빠지면안된다
                if board[new_rx][new_ry] == 'O':  # 그리고 빨간구슬이 빠졋다면 게임끝낸다
                    return depth
                # 이제 게임이 아직 끝나지 않았을 경우의 수를 계산한다
                if new_rx == new_bx and new_ry == new_by:  # 빨간구슬과 블루구슬의 위치가 같다면 좌표변경한다
                    if rcnt > bcnt:
                        new_rx -= dx
                        new_ry -= dy
                    else:
                        new_bx -= dx
                        new_by -= dy
                if not visited[new_rx][new_ry][new_bx][new_by]:  # 현재 위치가 체크된 백업이엇다면
                    visited[new_rx][new_ry][new_bx][new_by] = True  # 체크하고
                    queue.append((new_rx, new_ry, new_bx, new_by, depth + 1))  # 탐색 시작한다
    return -1


if __name__ == '__main__':
    row, col = map(int, input().split())
    board = [list(input().strip()) for _ in range(row)]
    visited = [[[[False] * col for _ in range(row)] for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx, ry = i, j
            if board[i][j] == 'B':
                bx, by = i, j
    print(bfs(rx, ry, bx, by))

import collections

n, m = map(int, input().split())
board = collections.defaultdict(list)
for num in range(n):
    board[num] = list(map(int, input()))
min_dist = 0


def bfs():
    global min_dist  # 함수 바깥에서 변수를 사용하고 싶을 때 global 키워드 사용
    queue = collections.deque()
    queue.append((0, 0, 1))  # 현재 위치 거리 1부터 시작
    dyx = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    while queue:
        cy, cx, cd = queue.popleft()
        if cy == n - 1 and cx == m - 1:
            min_dist = cd
            break
        for dy, dx in dyx:
            ny = cy + dy
            nx = cx + dx
            if ny >= 0 and nx >= 0 and ny < n and nx < m:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    queue.append((ny, nx, cd + 1))
bfs()

print(min_dist)

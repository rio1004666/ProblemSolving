import collections


def bfs(y, x):
    queue = collections.deque()
    queue.append((y, x))
    board[y][x] = 1
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in dyx:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    queue.append((ny, nx))


if __name__ == '__main__':
    n, m = map(int, input().split())
    # 이번에는 딕셔너리 자료구조로 그래프를 구현해보았습니다.
    board = collections.defaultdict(list)
    # 키값은 인덱스 0부터 시작합니다.
    dyx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 계속 index out of range뜨는데 어디서 문제엿냐했는데 여기서 .append()를 하면 리스트에 또 리스트가 이중으로 달게되서 문제엿다
    # 그냥 리스트자체를 넣을 때는 대입연산자(=) 쓰면된다
    for key in range(n):
        board[key] = list(map(int, input()))
    # print(board)
    # 이제 bfs탐색을 시작할 것입니다.

    result = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                continue
            else:
                bfs(y, x)
                result += 1
    print(result)

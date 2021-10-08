import collections


def stack_dfs(y, x):
    stack = []
    stack.append((y, x))
    graph[y][x] = 1
    while stack:
        cy, cx = stack.pop()  # 현재 노드를 빼고  그 노드에서 4가지 방향중 범위에 해당되고 방문하지 않은 노드를 방문해서 스택에 넣는다.
        for dy, dx in dyx:
            ny = cy + dy
            nx = cx + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                stack.append((ny, nx))

        # 이런식으로 하면 for문 나오자마자 빠져나가버린다 그다음 방문할 곳을 가지 못하고


n, m = map(int, input().split())
# 그래프를 딕셔너리 구조로 저장
graph = collections.defaultdict(list)
for key in range(n):
    graph[key] = list(map(int, input()))
result = 0

dyx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        result += 1
        # print(result,  ' 번째 스택 dfs 탐색')
        stack_dfs(i, j)
print(result)

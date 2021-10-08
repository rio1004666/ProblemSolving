
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(y, x):
    if y < 0 or x < 0 or y >= n or x >= m:
        return False
    if graph[y][x] == 0: # 한번 구멍을 발견하면 무조건 탐색이 끝난후 리턴값이 True가 된다.
        graph[y][x] = 1
        dfs(y, x + 1)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y - 1, x)
        return True
    return False # 구멍이 아닌 곳은 무조건 False를 반환하여 dfs탐색을 안한다.
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: # 범위를 벗어나거나 현재 위치가 1이면 False를 반환하는 식으로 풀이하였다
            result += 1
print(result)
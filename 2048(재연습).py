from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, queue = -1, deque()


def get(row, col):
    if board[row][col]:
        queue.append(board[row][col])
        board[row][col] = 0  # 큐에 넣고 0으로 셋팅해야한다 어차피 위로 이동하게 하면 그 자리는 블럭이 없어지기 때문이다.


def merge(row, col, drow, dcol):
    while queue:
        cur_block = queue.popleft()
        # 이제 경우의 수를 나눈다
        if not board[row][col]:  # 0인경우에는 놓아버린다.
            board[row][col] = cur_block
        elif board[row][col] == cur_block:  # 값이 일치한다면 2배로 증가해서 셋팅한다.
            board[row][col] = cur_block * 2
            # 두배로 증가시킨후에 좌표도 증가한다
            row, col = row + drow, col + dcol
        else:
            # 값이 일치하지않으면 그다음 좌표에 블럭을 둔다
            row, col = row + drow, col + dcol
            board[row][col] = cur_block


def move(k):  # 각 방향에 대해서 움직인다
    if k == 0:  # 위로 이동 , 즉 모든 블럭들이 위로 이동한다 그래서 column을 이동하면서 row를 전수검사한다
        for col in range(n):  # 컬럼이 고정이다.
            for row in range(n):  # row가 변경된다.
                get(row, col)
            # 한 컬럼이 큐에 다 넣어진다면 그다음 컬럼으로 넘어가기 전에 블럭합치기를 처리한다.
            merge(0, col, 1, 0)
    elif k == 1:  # 아래로 이동, 즉 모든 블럭들이 아래로 이동한다 column을 이동하면서 row를 전수 검사한다.
        for col in range(n):
            for row in range(n - 1, -1, -1):  # -1이전까지이므로 0까지 간다
                get(row, col)
            merge(n - 1, col, -1, 0)  # 아래로 내려가기 때문에 아래에서 부터 체크 해나가야한다.
    elif k == 2:  # 왼쪽으로 이동
        for row in range(n):
            for col in range(n):
                get(row, col)
            merge(row, 0, 0, 1)
    else:  # 오른쪽으로 이동
        for row in range(n):
            for col in range(n - 1, -1, -1):
                get(row, col)
            merge(row, n - 1, 0, -1)


def solve(count):
    global board, answer
    # 재귀적으로 움직인다 왜? 방향이 총 4가지 방향이므로 각각의 경우의 수 모두를 체크해야한다.
    if count == 5:
        for row in range(n):
            answer = max(answer, max(board[row]))
        return  # 카운팅이 5가 되는 순간 끝난다
    temp = [x[:] for x in board]  # 보드판 한 줄 씩 그대로 복사한다.
    for dir in range(4):
        move(dir)
        solve(count + 1)
        board = [x[:] for x in temp]


solve(0)
print(answer)

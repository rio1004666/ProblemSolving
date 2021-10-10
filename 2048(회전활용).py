from copy import deepcopy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def rotate(n, board):
    new_board = deepcopy(board)
    for row in range(n):
        for col in range(n):
            new_board[col][n - row - 1] = board[row][col]  # 0,2 가 2.3으로 된다
    return new_board


def convert(n, row):
    new_list = [num for num in row if num != 0]  # 다시 한줄에서 0이 아닌 수만 가져온다
    # 그런 후에 왼쪽으로 다 붙인 후에 나머지 0으로 채운다.
    for col in range(1, len(new_list)): # 현재 0이 아닌 숫자들만 뽑은 새로운 리스트에서 합쳐버린다.
        if new_list[col - 1] == new_list[col]:
            new_list[col - 1] = new_list[col] * 2
            new_list[col] = 0
    new_list = [num for num in new_list if num != 0]  # 이제 다 합쳐진 줄에서 나머지는 0으로 채운다
    return new_list + [0] * (n - len(new_list))  # 모두 왼쪽으로 이동후에 나머지는 0으로 채운다. (남은 갯수만큼)
    # 리스트 합침


def dfs(n, board, count):  # 상상을 해라 dfs는 최대한 각 경우의 수 가지들을 상상하면서 인자가 어떻게 넘어가고 반환값은 언제 나와야하는지 확인해야한다.
    result = max([max(row) for row in board])  # 각 줄마다 최댓값을 가져온 후에 최댓값만 모인 리스트의 최댓값을 다시 구한다.
    # 초기 보드판의 최댓값이 생성된다.
    if count == 0:  # 카운트를 다운시켜서 0이되면 최종적인 최댓값이 결정된다. 이 최종적인 최댓값을 가지고 다른 경우의 수들과 다시 비교해서 최댓값을 구할 것이다.
        return result
    for _ in range(4):
        merged_board = [convert(n, row) for row in board]  # 각 한줄 씩 가져와서 합친다.,
        result = max(result, dfs(n, merged_board, count - 1))
        board = rotate(n, board)

    return result


print(dfs(n, board, 5))

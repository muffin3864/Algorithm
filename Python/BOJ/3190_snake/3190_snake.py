import sys
<<<<<<< HEAD
from collections import deque
sys.stdin = open('input2.txt')

=======
sys.stdin = open('input2.txt')

from collections import deque
>>>>>>> 82b7109a8f7749c18e613949ce4a7494eae8daed
# 뱀은 맨위, 맨좌측에서 시작, 몸길이 = 1
# 뱀은 몸길이를 늘려 머리를 담칸에 위치
# 벽이나 자기자신에게 부딪히면 게임 끝
# 이동한 칸에 사과가 있으면, 사과가 없어지고 꼬리는 움직이지 않는다 -> 몸길이 증가
# 사과가 없으면 꼬리가 위치한 칸 비워준다 -> 몸길이 변화 x
# 게임이 몇초에 끝나는지 계산


# 보드의 크기
N = int(input())

# 사과의 개수
K = int(input())

# 보드판 생성
board = [[0] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과의 위치(x, y)
for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

# 뱀의 방향전환 횟수
L = int(input())

# 뱀의 몸길이 queue를 써서 앞에갚을 계속 꺼내서 위치 이동
snake = deque()
snake.append((0,0))

# 뱀의 방향전환 방향
direction = {}
for i in range(L):
    X, C = input().split()
    direction[int(X)] = C


# 뱀 시작위치에 지정
x, y = 0, 0
board[x][y] = 1

# 걸린시간
time = 0

# 방향 초기값
direct = 0

# 뱀 방향전환
def turn(alpha):
    global direct
    if alpha == 'L':
        direct = (direct - 1) % 4
    else:
        direct = (direct + 1) % 4

while True:
    time += 1
    x += dx[direct]
    y += dy[direct]

    # board 밖으로 나가면 끝
    if x < 0 or x >= N or y < 0 or y >= N:
        break

    # 사과를 만났을때 몸길이 증가
    if board[x][y] == 2:
        board[x][y] = 1
        snake.append((x, y))
        # 시간이 방향 딕셔너리에 들어있다면 방향 전환
        if time in direction:
            turn(direction[time])

    # 그냥 전진
    elif board[x][y] == 0:
        board[x][y] = 1
        # 이동한곳 좌표 추가
        snake.append((x, y))
        # 지나온곳 좌표 0으로 만들어놓기
        nx, ny = snake.popleft()
        board[nx][ny] = 0

        if time in direction:
            turn(direction[time])

    else:
        break

print(time)

import sys
sys.stdin = open('input.txt')


T = int(input())

# 오른쪽, 대각선, 아래
dx = [0, 1, 1]
dy = [1, 1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    kill = []
    for x in range(N-M+1):
        for y in range(N-M+1):
            fly = 0
            for i in range(M):
                for j in range(M):
                    fly += arr[x+i][y+j]

            kill.append(fly)


    print(f'#{tc} {max(kill)}')
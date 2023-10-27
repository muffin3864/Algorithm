import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]

    # 각 줄에 무슨 색으로 칠할지 고르기 위해 최소값 찾기
    change_color = []
    for row in flag:
        w = M - row.count('W')
        b = M - row.count('B')
        r = M - row.count('R')
        change_color.append([w, b, r])
    # print(change_color)
    result = 99999

    for w in range(0, N - 3 + 1):
        for b in range(1, N - 2 + 1 - w):
            r = N - w - b - 2

            # 정해진 라인 수 만큼 자신의 색깔로 바꾸는 카운트를 세어준다.
            cnt = 0
            for i in range(w):
                cnt += change_color[1:-1][i][0]
            for j in range(w, w + b):
                cnt += change_color[1:-1][j][1]
            for k in range(w + b, w + b + r):
                cnt += change_color[1:-1][k][2]

            # 최솟값을 찾고
            result = min(result, cnt)

    # 맨윗줄과 맨아랫줄도 바꿔준다.
    result += change_color[0][0] + change_color[-1][2]
    print(f'#{tc} {result}')



import sys
sys.stdin = open('input.txt')

# 1. 빈 배열을 만든다
# 2. 빈 배열을 순회하면서 각 색깔을 빈배열에 넣는다
# 3. 빈 배열에 3이 들어가 있는 칸 수를 센다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 빈 배열 생성
    arr = [[0] * 10 for _ in range(10)]

    for c in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 빈 배열 순회하면서 색칠하기
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color

    # arr 순회하면서 보라색이 칠해져 있는 칸 세기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')


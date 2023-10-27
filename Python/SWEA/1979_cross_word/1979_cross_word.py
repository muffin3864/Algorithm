import sys
sys.stdin = open('input.txt')

# 행과 열을 순회하면서 1이 K번 연속해서 있으면 count

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    # 행 체크
    for i in range(N):
        v_stack = []
        for j in range(N):
            if arr[i][j] == 1:
                v_stack.append(arr[i][j])

            elif arr[i][j] == 0 and len(v_stack) == K:
                cnt += 1
                v_stack.clear()

            elif arr[i][j] == 0:
                v_stack.clear()

        if len(v_stack) == K:
            cnt += 1


    # 열 체크
    for i in range(N):
        h_arr = []
        for j in range(N):
            h_arr.append(arr[j][i])

        h_stack = []
        for n in range(N):
            if h_arr[n] == 1:
                h_stack.append(arr[n])

            elif h_arr[n] == 0 and len(h_stack) == K:
                cnt += 1
                h_stack.clear()

            elif h_arr[n] == 0:
                h_stack.clear()

        if len(h_stack) == K:
            cnt += 1


    print(f'#{tc} {cnt}')


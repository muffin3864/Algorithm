import sys
sys.stdin = open('input.txt')

# 행, 열 검사해서 1이 연속으로 K만큼 정확한 갯수가 있으면 카운트
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    cnt = 0
    # 행 검사
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

    # 열 검사
    for i in range(N):
        y_list = []
        for j in range(N):
            y_list.append(arr[j][i])
        h_stack = []
        for k in range(N):
            if y_list[k] == 1:
                h_stack.append(y_list[k])
            elif y_list[k] == 0 and len(h_stack) == K:
                cnt += 1
                h_stack.clear()
            elif y_list[k] == 0:
                h_stack.clear()
        if len(h_stack) == K:
            cnt += 1
    print(f'#{tc} {cnt}')

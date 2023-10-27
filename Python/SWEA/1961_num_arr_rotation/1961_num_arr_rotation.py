import sys
sys.stdin = open('input.txt')

# 회전 시켜서 새로운 리스트에 넣는다
# 1열 => 1행, 2열 => 2행, 3열 => 3행
# 바뀔때 마다 스택에 쌓는다
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]


    # 90 회전
    degree90 = []
    for i in range(N):
        new_list = ''
        for j in range(N):
            new_list += arr[j][i]
        degree90.append(new_list[::-1])
    arr = degree90


    # 180 회전
    degree180 = []
    for i in range(N):
        new_list = ''
        for j in range(N):
            new_list += arr[j][i]
        degree180.append(new_list[::-1])
    arr = degree180


    # 270 회전
    degree270 = []
    for i in range(N):
        new_list = ''
        for j in range(N):
            new_list += arr[j][i]
        degree270.append(new_list[::-1])
    arr = degree270


    print(f'#{tc}')
    for i in range(N):
        print(degree90[i], degree180[i], degree270[i])


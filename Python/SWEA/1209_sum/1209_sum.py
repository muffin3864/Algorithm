import sys
sys.stdin = open('input.txt')

# 행, 열, 오른쪽 대각선, 왼쪽 대각선 의 합
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []
    # 각 행의 합
    for i in range(100):
        sum_list.append(sum(arr[i]))

    # 각 열의 합
    for i in range(100):
        column = []
        for j in range(100):
            column.append(arr[j][i])

        sum_list.append(sum(column))

    # 오른쪽으로 가는 대각선
    r_cross = []
    for i in range(100):
        for j in range(100):
            if i == j:
                r_cross.append(arr[i][j])
    sum_list.append(sum(r_cross))


    # 왼쪽으로 가는 대각선
    # (1,5), (2,4), (3,3), (4,2), (5,1) -> i += 1, j -= 1
    l_cross = []
    j = 99
    for i in range(100):
        l_cross.append(arr[i][j])
        j -= 1
    sum_list.append(sum(l_cross))

    print(f'#{tc} {max(sum_list)}')

import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]

    # 행 검사
    row = []
    for i in range(100):
        for N in range(100, -1, -1):    # 회문 길이
            for j in range(100-N+1):
                if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                    row.append(N)
                    break
    row_max = max(row)


    # 열 검사
    column = []
    for i in range(100):
        h_list = []
        for j in range(100):
            h_list.append(arr[j][i])

        for N in range(100, -1, -1):    # 회문 길이
            for j in range(100-N+1):
                if h_list[j:j+N] == h_list[j:j+N][::-1]:
                    column.append(N)
                    break
    column_max = max(column)

    if row_max >= column_max:
        print(f'#{tc} {row_max}')
    else:
        print(f'#{tc} {column_max}')

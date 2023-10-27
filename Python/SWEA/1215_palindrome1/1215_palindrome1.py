import sys
sys.stdin = open('input.txt')

# 배열에서 길이가 N인 회문 찾기
for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    cnt = 0
    for i in range(8):
        # 행 검색
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1

        # 열 검색
        y_list = []
        for j in range(8):
            y_list.append(arr[j][i])

        for k in range(8-N+1):
            if y_list[k:k+N] == y_list[k:k+N][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')

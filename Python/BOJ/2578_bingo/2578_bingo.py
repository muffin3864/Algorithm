# 빙고 찾기
def bingo():
    bingo = 0

    # 가로 확인
    for x in arr:
        if x.count(0) == 5:
            bingo += 1

    # 세로 확인
    for i in range(5):
        y = 0
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1

    # 왼쪽 위 대각선

    c1 = 0
    for i in range(5):
        if arr[i][i] == 0:
            c1 += 1
    if c1 == 5:
        bingo += 1

    # 오른쪽 위 대각선
    c2 = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            c2 += 1
    if c2 == 5:
        bingo += 1

    return bingo

arr = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

# 빙고 까지 걸리는 사회자의 최소 횟수
count = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc[i] == arr[x][y]:
                arr[x][y] = 0
                count += 1
    if count >= 12: # bingo가 외쳐지는 최소 값
        result = bingo()

        if result >= 3:
            print(i+1)
            break

# 2669.직사각형 네개의 합집합의 면적 구하기

# 9X9좌표 만들기
coord = [[0] * 100 for _ in range(100)]

for _ in range(4):
    # 직사각형의 좌표 받기
    x1, y1, x2, y2 = map(int, input().split())

    # 좌표에 직사각형 그리기
    for i in range(x1, x2):
        for j in range(y1, y2):
            # 그려진 부분 1로 바꾸기
            coord[i][j] = 1

# 좌표에 1로 적힌 부분 카운트
count = 0
for i in coord:
    count += sum(i)
print(count)
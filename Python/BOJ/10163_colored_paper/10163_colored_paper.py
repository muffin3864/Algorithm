import sys
sys.stdin = open('input1.txt')

N = int(input())
arr = [[0] * 101 for _ in range(101)]

# 범위만큼 순회하면서 각 색종이 칠해주기
for i in range(1, N + 1):
    x1, y1, w, h = map(int, input().split())

    for x in range(x1, x1 + w):
        for y in range(y1, y1 + h):
            arr[x][y] = i

# 색종이 별로 칠해진 숫자 찾아서 카운트 해주기
count = [0] * (N+1) # 범위 안벗어나기 위해 안전하게 0추가
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            count[arr[i][j]] += 1

# 추가 해주었던 0 제거
count.remove(0)

for i in count:
    print(i)


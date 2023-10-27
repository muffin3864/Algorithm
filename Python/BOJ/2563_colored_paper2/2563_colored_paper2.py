import sys
sys.stdin = open('input.txt')

# 색종이 크기 10x10 고정
# 붙인 색종이 넓이 구하기

N = int(input())
arr = [[0] * 100 for _ in range(100)]

for k in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            # 시작지점으로부터 10칸씩 채우기
            arr[i][j] = 1

cnt = 0
for i in arr:
    cnt += i.count(1)

print(cnt)
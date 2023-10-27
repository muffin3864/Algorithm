import sys
sys.stdin = open('input.txt')

# 제일 긴 값 찾자
# 긴 값 기준으로 작은 값들 추가 할때마다 1로 채우기

N = int(input())
arr = [0 for _ in range(1001)]

for i in range(N):
    x, h = map(int, input().split())
    arr[x] = h

# 제일 긴 값 찾기
max_idx = arr.index(max(arr))
# 왼쪽에서 부터 넓이 채우기
max_val = 0
for i in range(max_idx):
    max_val = max(max_val, arr[i])
    arr[i] = max_val
# 오른쪽에서 부터 넓이 채우기
max_val = 0
for i in range(1000, max_idx, -1):
    max_val = max(max_val, arr[i])
    arr[i] = max_val

print(sum(arr))


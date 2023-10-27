import sys
sys.stdin = open('input.txt')

# 1,2 가로, 3,4 세로

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
w = 0
w_idx = 0
h = 0
h_idx = 0
# 작은 길이 구하기
for i in range(6):
    # 가로
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            w_idx = i
    # 세로
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if h < arr[i][1]:
            h = arr[i][1]
            h_idx = i
# 큰 길이 구하기
W = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
H = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])

result = ((w * h) - (W * H)) * K
print(result)
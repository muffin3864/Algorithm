import sys
sys.stdin = open('input.txt')

# N개의 랜선 필요
# 길이가 제각각인 K개의 랜선에서 길이가 같은 N개가 되도록 자른다.(남는 부분은 버림)
# 이진탐색으로 풀자

K, N = map(int, input().split())
len_list = []
for _ in range(K):
    len_list.append(int(input()))

start = 1
end = max(len_list)

while start <= end:
    mid = (start + end) // 2

    # mid크기로 잘라서 몇개 나오는지 카운트
    cnt = 0
    for i in len_list:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
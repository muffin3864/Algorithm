import sys
sys.stdin = open('input2.txt')
# 나무 M미터가 필요
# 절단기에 H를 지정하면 윗부분이 짤림
# 나무 여러개를 동시에 짤라서 M만큼만 가져간다
# 이진탐색으로 풀자

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

# start와 end가 같아질때 까지 반복
while start <= end:
    mid = (start + end) // 2

    # 벌목 나무 총 합
    need = 0
    for i in trees:
        # 나무의 높이가 절단기 보다 높으면
        if i >= mid:
            need += i - mid

    # 자른 나무들의 길이가 목표값 이상이면
    if need >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
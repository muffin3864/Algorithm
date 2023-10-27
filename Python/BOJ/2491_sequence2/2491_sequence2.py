import sys
sys.stdin = open('input3.txt')

N = int(input())
num = list(map(int, input().split()))

# 길이의 최소는 1이기 때문에 1부터 시작
result = 1
increase = 1
decrease = 1
# 연속되는 수가 연속해서 커지거나 작아지면 그 길이 출력

# 수가 연속해서 커질때(길이 1을 넣어놨으므로 1부터)
for i in range(1, N):
    if num[i-1] <= num[i]:
        increase += 1
        if increase > result:
            result = increase
        else:
            result
    else:
        increase = 1

# 수가 연속해서 작아질때
for i in range(1, N):
    if num[i-1] >= num[i]:
        decrease += 1
        if decrease > result:
            result = decrease
        else:
            result
    else:
        decrease = 1

print(result)
import sys
sys.stdin = open('input2.txt')

text = list(input())

# 양끝부터 동시에 체크하는 횟수
N = len(text)
check = N // 2
result = 1

for i in range(check):
    if text[i] != text[N - 1 - i]:
        result = 0

print(result)
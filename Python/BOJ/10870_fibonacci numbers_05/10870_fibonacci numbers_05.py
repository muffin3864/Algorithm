import sys
sys.stdin = open('input.txt')

# 피보나치 수는 0과 1로 시작
# 다음 2번째 부터는 바로 앞 두 피보나치 수의 합

n = int(input())

# 0과 1로 시작
arr = [0, 1]

for i in range(N):

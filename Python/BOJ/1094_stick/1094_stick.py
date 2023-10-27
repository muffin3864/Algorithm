import sys
sys.stdin = open('input1.txt')

# 막대기의 길이 0 < X <= 64
# 모든 막대의 길이 합이 X보다 크면
# 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자름
# 절반 중 하나를 버리고 남아있는 막대의 합이 x보다 크거나 같으면 위에서 자른 막대의
# 절반 중 하나를 버림
# 남아있는 막대의 합으로 x를 만든다
# 막대 몇개인지 출력

x = int(input())

cnt = 0

while x > 0:
    if x & 1:
        cnt += 1
    x >>= 1
print(cnt)


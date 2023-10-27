import sys
sys.stdin = open('input.txt')

# N개의 문자열로 이루어진 집합 S
# M개의 문자열 중 집합 S에 포함되어 있는 것이 총 몇개인지 출력

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())

cnt = 0
for _ in range(M):
    string = input()
    if string in S:
        cnt += 1

print(cnt)
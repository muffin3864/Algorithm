import sys
sys.stdin = open('input.txt')

# N개의 탑을 세운다
# 리스트 왼쪽에서 시작, 스택에 있는 값이 현재 타워보다 크면 리스트에 추가

N = int(input())
tower = list(map(int, input().split()))
reception = [0] * N
stack = []
# [6, 9, 5, 7, 4]
for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]: # 높이 비교
            reception[i] = stack[-1][0] + 1 # 인덱스 값, 탑의 위치는 1부터 시작이기 때문에 +1 해줌
            break
        else:
            stack.pop()

    stack.append([i, tower[i]])

print(*reception)

# [0, 0, 2, 2, 4]
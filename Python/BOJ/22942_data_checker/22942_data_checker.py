import sys
sys.stdin = open('input2.txt')
# 모든 원의 중심 좌표는 x축 위에 존재
# N개의 원 중 임의로 두 원을 선택했을때, 교점이 없어야 한다.
# -> 하나의 원이 다른 원 안에 존재하거나 외부에 존재
# 두번째 조건만 만족하는지 확인
# 데이터가 조건에 맞으면 YES, 만족하지 않으면 NO를 출력

N = int(sys.stdin.readline())
# 원의 좌표를 리스트로 만들어서 비교
circle = []

# 원의 좌표 끝부분을 따로 받음
for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circle.append((x - r, i))
    circle.append((x + r, i))

circle.sort()

# 스택에 좌표를 넣어서 겹치는게 있으면 제거
stack = []
for i in circle:
    if stack:
        if stack[-1][1] == i[1]:
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

# 스택에 좌표가 남아있으면 교점이 있는것
if stack:
    print('NO')
else:
    print('YES')

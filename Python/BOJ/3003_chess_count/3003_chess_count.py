import sys
sys.stdin = open('input1.txt')

# 체스 개수 찾기
# 부족한 건 몇개 부족한지, 많은건 몇개 빼야하는지 출력

chess = list(map(int, input().split()))

need = []

# 0: 킹, 1: 퀸, 2: 룩, 3: 비숍, 4: 나이트, 5: 폰
if chess[0] == 1:
    need.append(0)
elif chess[0] > 1:
    need.append(-(chess[0] - 1))
else:
    need.append(abs(chess[0]-1))

if chess[1] == 1:
    need.append(0)
elif chess[1] > 1:
    need.append(-(chess[1] - 1))
else:
    need.append(abs(chess[1]-1))

if chess[2] == 2:
    need.append(0)
elif chess[2] > 2:
    need.append(-(chess[2] - 2))
else:
    need.append(abs(chess[2]-2))

if chess[3] == 2:
    need.append(0)
elif chess[3] > 2:
    need.append(-(chess[3] - 2))
else:
    need.append(abs(chess[3]-2))

if chess[4] == 2:
    need.append(0)
elif chess[4] > 2:
    need.append(-(chess[4] - 2))
else:
    need.append(abs(chess[4]-2))

if chess[5] == 8:
    need.append(0)
elif chess[5] > 8:
    need.append(-(chess[5] - 8))
else:
    need.append(abs(chess[5]-8))

print(*need)
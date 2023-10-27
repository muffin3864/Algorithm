import sys
sys.stdin = open('input.txt')

# N개의 물건
# 물건은 무게 W와 가치 V를 가짐
# 준서의 최대 무게는 K
# 물건들의 가치합의 최대값 출력


N, K = map(int, input().split())    # N: 물품의 수, K: 최대 무게
items = [[0, 0]]
bag = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(N):
    items.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = items[i][0]
        value = items[i][1]

        if j < weight:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[N][K])

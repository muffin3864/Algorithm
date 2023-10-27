import sys
sys.stdin = open('input.txt')

# 당근 크기 별로 소, 중, 대 로 나누어 상자에 담는다.
# 상자 비어있으면 X
# 한 상자에 N/2개 초과 하면 안됨(절반)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    carrot.sort()
    min_v = 1000
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                small = i + 1
                mid = j - i
                large = N - 1 - j
                if small <= N // 2 and mid <= N // 2 and large <= N // 2:
                    if min_v > (max(small, mid, large) - min(small, mid, large)):
                        min_v = (max(small, mid, large) - min(small, mid, large))
    if min_v == 1000:
        min_v = -1
    print(f'#{tc} {min_v}')

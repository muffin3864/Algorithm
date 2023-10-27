import sys
sys.stdin = open('input.txt')

T = int(input())

# N = 손님수, M = 만드는 시간, K = 만드는 붕어빵 개수
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort()
    result = 'Possible'
    for i in range(N):
        fish = (guest[i] // M) * K - (i + 1)

        if fish < 0 :
            result = 'Impossible'

    print(f'#{tc} {result}')




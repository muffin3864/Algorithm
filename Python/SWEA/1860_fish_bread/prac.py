import sys
sys.stdin = open('input.txt')

# 시간이 지나면 붕어빵 K개 만들어짐, 사람이 오면 붕어빵 1개 감소
# 사람이 왔을때 붕어빵 없으면 impossible, 있으면 possible
# N = 사람수
# M = 붕어빵 만드는데 걸리는 시간
# K = 붕어빵이 한번에 만들어지는 갯수
# customer = 손님이 오는 시간
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort() # 손님 오는 시간 오름차순

    result = 'Possible'

    for i in range(N):
        fish = (customer[i] // M) * K

        if fish < i + 1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')




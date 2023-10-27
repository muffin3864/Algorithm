import sys
sys.stdin = open('input.txt')

def check(number):
    num = list(str(number))
    i = 0
    while i < len(num) -1:
        if num[i] > num[i+1]:
            return False
        i += 1
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1

    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if result < num and check(num):
                result = num
    print(f'#{tc} {result}')
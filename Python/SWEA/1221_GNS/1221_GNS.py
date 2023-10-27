import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    tc, N = input().split()
    arr = list(map(str, input().split()))
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = ''

    for n in numbers:
        for i in arr:
            if n == i:
                result += i + ' '
    print(tc)
    print(result)

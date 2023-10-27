import sys
sys.stdin = open('input.txt')


# NxN 체스판에 퀸을 N개 놓는다.
# 퀸 N개가 서로 공격할 수 없게 놓는 경우의 수 출력

N = int(input())
result = 0
row = [0] * N


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global result
    if x == N:
        result += 1
        return

    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)

print(result)
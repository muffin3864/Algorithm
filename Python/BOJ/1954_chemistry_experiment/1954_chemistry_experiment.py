from itertools import product
import sys
sys.stdin = open('input2.txt')

# n가지 종류의 시약 t
# M mg의 용액
# M의 x mg 실험
# 가스 = a * x + b
# 같은 양의 가스 발생 하면 가스 양 출력
# 다른 양의 가스 발생 하면 0 출력


def experiment(A, B):

    comb = []
    for combo in product(range(M), repeat=n):
        if sum(combo) == M:
            comb.append(combo)

    temp = 0
    for X in comb:
        gas = []
        for j in range(n):
            a, b = A[j], B[j]
            make_gas = a * X[j] + b
            gas.append(make_gas)

        if len(list(set(gas))) == 1:
            temp = gas[0]
            break
        else:
            temp = 0

    return temp


n = int(input())

reagent_a = []
reagent_b = []
for i in range(n):
    a, b = map(int, input().split())
    reagent_a.append(a)
    reagent_b.append(b)

M = int(input())

result = experiment(reagent_a, reagent_b)

print(result)


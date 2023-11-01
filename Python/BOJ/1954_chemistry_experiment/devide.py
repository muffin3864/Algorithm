import sys
sys.stdin = open('input2.txt')

from itertools import product


def experiment(A, B, M, n):
    max_gas = 0  # 최대 가스 양 초기화

    for combo in product(range(M + 1), repeat=n):
        if sum(combo) == M:
            gas_values = [a * combo[j] + b for j, (a, b) in enumerate(zip(A, B))]
            same_gas = all(g == gas_values[0] for g in gas_values)
            if same_gas:
                max_gas = max(max_gas, gas_values[0])

    if max_gas > 0:
        return max_gas
    else:
        return 0


n = int(input())

reagent_a = []
reagent_b = []

for i in range(n):
    a, b = map(int, input().split())
    reagent_a.append(a)
    reagent_b.append(b)

M = int(input())

result = experiment(reagent_a, reagent_b, M, n)

print(result)
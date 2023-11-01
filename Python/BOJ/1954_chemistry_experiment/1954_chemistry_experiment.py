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



# sol


# arr = []
# ans = 0

# N = int(input())

# for _ in range(N):
#     arr.append(tuple(map(int, input().split())))
# M = int(input())

# # N = 1인 경우 따로 처리
# if N == 1:
#     ans = arr[0][0]*M + arr[0][1]

# if ans == 0:
#     # 제일 큰 애부터 숫자 넣을거라서 a 내림차순으로 정렬
#     arr.sort(reverse=True)
#     # print(arr)

#     # 제일 큰애한테 쓸 약품
#     for i in range(1, M-N+1):
#         # 사용한 약품 양
#         acc = i
#         # print('i', i)
#         maxi = arr[0][0]*i + arr[0][1]
#         for j in range(1, N):
#             if (maxi-arr[j][1]) % arr[j][0]:
#                 # 자연수 아니면 다음조사로 넘어가
#                 # 전부 continue 였다가 아니어서 바꿈!
#                 break
#             tmp = (maxi-arr[j][1]) // arr[j][0]
#             # 자연수가 아닌경우 넘어가
#             if tmp <= 0:
#                 break
#             # 자연수일 경우, 약물 사용 누적합 구하기
#             acc += tmp
#             # print('j, x, maxi', j, tmp, maxi)
#             # 용량 초과면 돌아가
#             if acc > M:
#                 break
#             # 마지막 약품 조사하고, 누적합이 약물양이라면 성공
#             if j == N-1 and acc==M:
#                 ans = maxi
#                 break
#         # 답을 구했다면 조사 더이상 하지마!
#         if ans != 0:
#             break
# print(ans)



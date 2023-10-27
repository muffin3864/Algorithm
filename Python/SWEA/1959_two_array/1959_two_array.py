import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    # A,B 둘 중 작은것이 움직이게 한다
    # 큰것에서 작은것을 뺀만큼 움직임 (7 - 6 = 1)
    result = 0
    if len(A_list) - len(B_list) < 0:
        multi_sum = []
        for i in range(len(B_list) - len(A_list)+1):  # 작은 배열이 움직이는 횟수
            multi = []
            for j in range(len(A_list)):    # 배열의 각 요소끼리 비교해서 곱하기
                multi.append(B_list[i+j] * A_list[j])
            multi_sum.append(sum(multi))
        result = max(multi_sum)

    elif len(A_list) - len(B_list) > 0:
        multi_sum = []
        for i in range(len(A_list) - len(B_list) + 1):  # 작은 배열이 움직이는 횟수
            multi = []
            for j in range(len(B_list)):  # 배열의 각 요소끼리 비교해서 곱하기
                multi.append(A_list[i + j] * B_list[j])
            multi_sum.append(sum(multi))
        result = max(multi_sum)
    else:   # 길이가 같은때
        multi = []
        for i in range(len(A_list)):
            multi.append(A_list[i] * B_list[i])
        result = sum(multi)

    print(f'#{tc} {result}')
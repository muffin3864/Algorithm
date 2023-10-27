import sys
sys.stdin = open('input.txt')

# 기준이 되는 지점의 양쪽 2칸안에 제일 큰값이 기준보다 작으면 그 차이만큼 카운트

for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    cnt = 0
    for i in range(2,N-2):
        b_list = []
        for j in range(i-2, i+3):
            b_list.append(building[j])
        b_list.pop(2)

        if building[i] > max(b_list):
            cnt += building[i] - max(b_list)

    print(f'#{tc} {cnt}')


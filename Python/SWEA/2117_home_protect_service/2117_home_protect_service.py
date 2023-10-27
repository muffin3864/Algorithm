import sys
sys.stdin = open('input.txt')

# 마름모 영역에서 서비스 제공
# 마름모가 커질수록 운영비 커짐 = 마름모의 넓이가 운영비용
# K=1 운영비용=1, K=2 운영비용=5, K=3 운영비용=13
# 보안회사 이익 = 서비스 제공받는 집들의 수익(집 갯수 * 고객비용) - 운영비용 > 0 , OK


# 1. 마름모꼴로 움직이면서 배열 순회
# 2. 마름모 안에 집들어오면 갯수 세기
# 3. 보안회사가 손해를 안보는지 체크
# 4. 손해 안보면 집 갯수 리스트에 넣어놓기
# 5. 손해 안보는 집 갯수 중 제일 집 많은 값
# 6. 마름모 크기 1씩 늘리면서 반복


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    max_house = 0

    # 마름모 K에 따라 크기 만들기
    for k in range(1, N + 2):
        cost = k ** 2 + (k - 1) ** 2    # 비용

        dia = []    # 마름모 크기 저장 리스트

        # k가 증가 할때 마다 마름모 위치 저장(delta함수 마냥)
        for i in range(k):
            for j in range(-k+1+i, k-i):
                if i == 0:
                    dia.append((i, j))
                else:
                    dia.append((i, j))
                    dia.append((-i, j))
        # print(dia)

        # 마름모가 순회하면서 집 세기
        for i in range(N):
            for j in range(N):
                house = 0
                for l in dia:
                    di, dj = l
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and city[ni][nj] == 1:
                        house += 1

                profit = house * M

                if profit >= cost:  # 손해만 보지 않으면 되므로 이득 >= 비용이다.
                    if house > result:  # 이 때 temp가 answer보다 크면 answer로 바꿔줌
                        result = house
    print(f'#{tc} {result}')

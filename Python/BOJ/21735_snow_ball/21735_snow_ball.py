import sys
sys.stdin = open('input.txt')

# 앞마당 길이 N, 위치 1부터 N 까지만 눈 있음
# 위치 i에 a만큼 눈이 쌓여있음
# M초 동안 눈덩이 굴려 눈사람 만들기
# 눈덩이 시작크기 = 1, 눈덩이 시작 위치 = 0
# 눈덩이 굴리거나 던질 때 1초 소모
# 위치 +1만큼 굴린다, 눈덩이 크기 a(i+1) 만큼 늘어남
# 위치 +2만큼 던진다, 눈덩이 크기 a(i+2) 만큼 늘어남
# 던질때 눈덩이 반으로 줄어듬
# 눈덩이를 던져 크기가 0이되도 사라지지 않음
# 눈덩이가 앞마당 끝에 도달하면 시간과 상관 없이 끝남
# 대회 시간 내에 가장 큰 눈덩이 크기 구하기


def roll(idx, size, time):
    global result
    size += a[idx]

    # 시간이 다 되면 스탑
    if time == M:
        result = max(result, size)
        return

    # 도착점에 도착하면 스탑
    if idx == N - 1:
        result = max(result, size)
        return

    # 굴릴 때
    if idx + 1 < N:
        roll(idx + 1, size, time + 1)

    # 던질 때때
    if idx + 2< N:
        roll(idx + 2, size // 2, time + 1)


N, M = map(int, input().split())
a = list(map(int, input().split()))
result = 0
# 그냥 0에서 시작
roll(0, 1, 1)

# N이 1보다 크면 던지는거 부터 가능하기 때문에 넣어둠
if N > 1:
    roll(1, 0, 1)
print(result)
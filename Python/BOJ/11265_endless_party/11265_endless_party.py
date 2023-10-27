import sys
sys.stdin = open('input.txt')

# N개의 파티장
# 도로들은 일방 통행
# c만큼의 시간안에 B파티장에 갈 수 있는가?, 없는가?


N, M = map(int, input().split())
time_arr = [list(map(int, input().split())) for _ in range(N)]
# 플로이드 워셜 써서 최단기록으로 갱신 해줌
for k in range(N):
    for i in range(N):
        for j in range(N):
            if time_arr[i][j] > time_arr[i][k] + time_arr[k][j]:
                time_arr[i][j] = time_arr[i][k] + time_arr[k][j]
# print(time_arr)
for _ in range(M):
    A, B, C = map(int, input().split()) # A = now, B = next, C = next party start
    
    time = time_arr[A-1][B-1]
    if time > C:
        print('Stay here')
    else:
        print('Enjoy other party')
    

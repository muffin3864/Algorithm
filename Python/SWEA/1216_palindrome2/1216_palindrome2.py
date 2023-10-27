import sys
sys.stdin = open('input.txt')

# 회문길이가 큰것을 찾는것이므로 N을 큰값부터 집어넣어 회문을 찾으면 break
for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]
    # 가로
    v_len = []
    for i in range(100):
        for N in range(100,-1,-1):
            for j in range(100 - N + 1):
                if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                    v_len.append(N)
                    break
    v_max = max(v_len)


    # 세로
    h_len = []
    for i in range(100):
        h = []
        for j in range(100):
            h.append(arr[j][i])

        for N in range(100, -1, -1):
            for y in range(100 -N + 1):
                if h[y:y+N] == h[y:y+N][::-1]:
                    h_len.append(N)
                    break
    h_max = max(h_len)


    if v_max >= h_max:
        print(f'#{tc} {v_max}')
    else:
        print(f'#{tc} {h_max}')


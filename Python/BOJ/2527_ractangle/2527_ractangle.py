import sys
sys.stdin = open('input.txt')

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # 공통부분 X = d
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
        continue

    # 점 = c
    elif p1 == x2 or p2 == x1:
        if q1 == y2 or q2 == y1:
            print('c')
            continue
        # 선분 = b
        else:
            print('b')
            continue
    elif q1 == y2 or q2 == y1:
        print('b')
        continue
    # 직사각형 = a
    else:
        print('a')
        continue

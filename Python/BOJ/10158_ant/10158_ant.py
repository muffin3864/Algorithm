import sys
sys.stdin = open('input2.txt')


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# t초 만큼 움직인다 = 1초에 1칸씩 이동
# x, y 는 증가하거나 감소하거나 둘 중 하나
x = (p + t) // w
y = (q + t) // h

# x좌표
if x % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

# y좌표
if y % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)

W, H = map(int, input().split())
field = [[0] * (W+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [[0] * (W+2)]
even_move = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
odd_move = [(-1, 1), (-1, 0), (0, -1), (0, 1), (1, 1), (1, 0)]

def valid(y, x):
    return 0 <= y < H+2 and 0 <= x < W+2

seen = [[0] * (W+2) for _ in range(H+2)]
deq = deque()
deq.append((0, 0))
seen[0][0] = 1
ans = 0
while deq:
    y, x = deq.popleft()
    if y%2:
        dydx = odd_move
    else:
        dydx = even_move
    
    for a, b in dydx:
        nexty = y+a
        nextx = x+b
        if valid(nexty, nextx):
            if field[nexty][nextx]:
                ans += 1
            else:
                if seen[nexty][nextx]:continue
                seen[nexty][nextx] = 1
                deq.append((nexty, nextx))
print(ans)


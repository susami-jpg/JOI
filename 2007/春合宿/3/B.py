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
eps = 0.0000000001
#input = stdin.readline

N, M = map(int, input().split())
v = [tuple(map(int, input().split())) for _ in range(N)]
v.append((INF, INF))
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((b, c))
    edge[b].append((a, c))

dist = [[INF] * (N+1) for _ in range(N)]
fix = [[False] * (N+1) for _ in range(N)]
dist[0][N] = 0
hq = [(0, 0, N)]

def can_go(prev, cur, nxt):
    if prev == (INF, INF):
        return True
    a1, a2 = prev[0]-cur[0], prev[1]-cur[1]
    b1, b2 = nxt[0]-cur[0], nxt[1]-cur[1]
    if a1*b1+a2*b2 <= 0:
        return True
    else:
        return False
    
while hq:
    _, cur, prev = heappop(hq)
    fix[cur][prev] = True
    for nxt, cost in edge[cur]:
        if not fix[nxt][cur] and can_go(v[prev], v[cur], v[nxt]):
            dist[nxt][cur] = min(dist[nxt][cur], dist[cur][prev] + cost)
            heappush(hq, (dist[nxt][cur], nxt, cur))

ans = min(dist[1])
if ans == INF:
    print(-1)
else:
    print(ans)


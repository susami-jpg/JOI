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

N = int(input())
M = int(input())
edge = [[] for _ in range(N)]
degree = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    degree[b] += 1

deq = deque()
for v in range(N):
    if degree[v] == 0:
        deq.append(v)

ans = []
ok = False
while deq:
    if len(deq) >= 2:
        ok = True
    v = deq.popleft()
    ans.append(v+1)
    for nextv in edge[v]:
        degree[nextv] -= 1
        if degree[nextv] == 0:
            deq.append(nextv)
for v in ans:
    print(v)
print(int(ok))

        


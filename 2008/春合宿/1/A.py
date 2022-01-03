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
G = [0] * N
edge = [[] for _ in range(N)]
for i in range(N):
    p, g = map(int, input().split())
    if p == 0:
        root = i
    else:
        p -= 1
        edge[p].append(i)
    G[i] = g

dp1 = [-INF]*N
def dfs1(v, par=-1):
    pm = 0
    for nextv in edge[v]:
        if nextv == par:continue
        dfs1(nextv, v)
        pm += max(dp1[nextv], 0)
    dp1[v] = pm + G[v]
    return

#dp2 = [-INF]*N
#vを含まずに、rootの親方向のdpを集計
"""
def dfs2(v, par=-1):
    cn = len(edge[v])
    left = [-INF]*(cn+1)
    right = [-INF]*(cn+1)
    left[0] = 0
    right[-1] = 0
    for i in range(cn):
        cl = edge[v][i]
        cr = edge[v][cn-i-1]
        if cl == par:
            left[i+1] = left[i]
        if cr == par:
            right[cn-i-1] = right[cn-i]
        else:
            left[i+1] = max(0, dp1[cl]) + left[i]
            right[cn-i-1] = max(0, dp1[cr]) + right[cn-i]
    for i in range(cn):
        c = edge[v][i]
        if c == par:continue
        rest = left[i] + right[i+1]
        rest += max(0, dp2[v]) + G[v]
        dp2[c] = rest
        dfs2(c, v)
    return
"""

dfs1(0)
#dfs2(0)
ans = -INF
for v in range(N):
    ans = max(ans, dp1[v])
print(ans)

        
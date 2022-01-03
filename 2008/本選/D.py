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
rec = [[] for _ in range(N+3)]
col_set = set()
for i in range(1, N+1):
    inp = list(map(int, input().split()))
    k = inp[0]
    for j in range(1, k+1):
        rec[i].append(tuple(inp[2*j-1:2*j+1]))
        c = inp[2*j-1]
        col_set.add(c)

def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(set(A))):
        B[i] = j
        C[j] = i
    return B, C

ind_to_col, col_to_ind = CC(col_set)
W = len(ind_to_col) 
for j in range(W):
    rec[0].append((ind_to_col[j], 0))
    rec[N+1].append((ind_to_col[j], 0))       

p = dp1 = dp2 = [[INF] * (M+1) for _ in range(W)]
for j in range(W):
    dp1[j][0] = 0
for i in range(N+1):
    p = dp1
    dp1 = dp2
    dp2 = [[INF] * (M+1) for _ in range(W)]
    for j1, c1 in rec[i]:
        ji1 = col_to_ind[j1]
        for k in range(M+1):
            if p[ji1][k] == INF:continue
            for j2, c2 in rec[i+1]:
                ji2 = col_to_ind[j2]
                dp1[ji2][k] = min(dp1[ji2][k], p[ji1][k] + (c1+c2)*abs(j1-j2))
            for j2, c2 in rec[i+2]:
                if k+1 > M:continue
                ji2 = col_to_ind[j2]
                dp2[ji2][k+1] = min(dp2[ji2][k+1], p[ji1][k] + (c1+c2)*abs(j1-j2))

ans = INF
for j in range(W):
    for k in range(M+1):
        ans = min(ans, dp1[j][k])
print(ans)

        

    
    
    
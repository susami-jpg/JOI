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

def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(A)):
        B[i] = j
        C[j] = i
    return B, C

N = int(input())
A, B = map(int, input().split())
h_set = set()
w_set = set()
origami = []
for _ in range(N):
    p, q, r, s = map(int, input().split())
    h_set.add(p)
    h_set.add(p+1)
    h_set.add(r)
    h_set.add(r+1)
    w_set.add(q)
    w_set.add(q+1)
    w_set.add(s)
    w_set.add(s+1)
    origami.append((p, q, r, s))
    
h_set.add(0)
h_set.add(A)
h_set.add(A+1)
w_set.add(0)
w_set.add(B)
w_set.add(B+1)
ind_to_h, h_to_ind = CC(list(h_set))
ind_to_w, w_to_ind = CC(list(w_set))

H = len(h_set)
W = len(w_set)
field = [[0] * W for _ in range(H)]
for p, q, r, s in origami:
    p = h_to_ind[p]
    r = h_to_ind[r]
    q = w_to_ind[q]
    s = w_to_ind[s]
    field[p][q] += 1
    field[p][s+1] -= 1
    field[r+1][q] -= 1
    field[r+1][s+1] += 1

for i in range(H):
    for j in range(1, W):
        field[i][j] += field[i][j-1]

for j in range(W):
    for i in range(1, H):
        field[i][j] += field[i-1][j]
    
max_dub = 0
for i in range(H):
    for j in range(W):
        max_dub = max(max_dub, field[i][j])

ans = 0
for i in range(H-1):
    for j in range(W-1):
        if field[i][j] == max_dub:
            ans += (ind_to_h[i+1] - ind_to_h[i]) * (ind_to_w[j+1] - ind_to_w[j])
print(max_dub)
print(ans)

"""
4 
8 6 
2 4 3 6
5 1 6 6
2 5 8 5
1 2 5 3
"""
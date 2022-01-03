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

H, W = map(int, input().split())
JOI = [list(" " * (W+2))] + [list(" " + input() + " ") for _ in range(H)] + [list(" " * (W+2))]
mark = list(input() + input())
def is_mark(i, j):
    return JOI[i][j:j+2] + JOI[i+1][j:j+2] == mark
    
cnt = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if is_mark(i, j):
            cnt += 1

ans = cnt
dxdy = [(-1, -1), (0, -1), (-1, 0), (0, 0)]
for i in range(1, H+1):
    for j in range(1, W+1):
        p = cnt
        pi = JOI[i][j]
        for c in ["J", "O", "I"]:
            if JOI[i][j] == c:continue
            for a, b in dxdy:
                ni = i+a
                nj = j+b
                if is_mark(ni, nj):
                    p -= 1
            JOI[i][j] = c
            for a, b in dxdy:
                ni = i+a
                nj = j+b
                if is_mark(ni, nj):
                    p += 1
            ans = max(ans, p)
        JOI[i][j] = pi
print(ans)



        
        
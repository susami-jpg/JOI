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
eps = 0.00000000001
setrecursionlimit(10**7)
input = stdin.readline

N, W, H = map(int, input().split())
plots = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if len(set([i, j, k, l])) != 4:continue
                A = plots[i]
                B = plots[j]
                C = plots[k]
                D = plots[l]
                r1 = (A[0]-B[0])**2 + (A[1]-B[1])**2
                r2 = (C[0]-D[0])**2 + (C[1]-D[1])**2
                dac = (A[0]-C[0])**2 + (A[1]-C[1])**2
                if r1-r2-dac >= 0 and (r1-r2-dac)**2 > 4*r2*dac and A[0]**2 >= r1 and A[1]**2 >= r1 and (W-A[0])**2 >= r1 and (H-A[1])**2 >= r1:
                    ans += 1
print(ans)

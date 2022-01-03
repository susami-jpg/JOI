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

N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N+1)]
B = [0] * (N)
for i in range(1, N+1):
    B[i-1] = A[i]-A[i-1]

cur = 0
for i in range(N):
    if B[i] > 0:
        cur += -S*B[i]
    else:
        cur += -T*B[i]

for _ in range(Q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    pl = B[l]
    B[l] += x
    if pl <= 0 and B[l] <= 0:
        cur += (B[l]-pl)*(-T)
    elif pl > 0 and B[l] > 0:
        cur += (B[l]-pl)*(-S)
    elif pl > 0 and B[l] <= 0:
        cur += pl*S
        cur += -B[l]*T
    else:
        cur += pl*T
        cur += -B[l]*S
        
    if r+1 < N:
        pr = B[r+1]
        B[r+1] -= x
        if pr <= 0 and B[r+1] <= 0:
            cur += (B[r+1]-pr)*(-T)
        elif pr > 0 and B[r+1] > 0:
            cur += (B[r+1]-pr)*(-S)
        elif pr > 0 and B[r+1] <= 0:
            cur += pr*S
            cur += -B[r+1]*T
        else:
            cur += pr*T
            cur += -B[r+1]*S
    print(cur)

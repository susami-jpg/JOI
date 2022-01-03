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
A = list(map(int, input().split()))
rec = defaultdict(list)
for i in range(N):
    rec[A[i]].append(i)

ans = 0
prev = ans
seen = [0] * N
for key, P in sorted(rec.items(), reverse=True):
    cnt = prev
    if key == 0:
        break
    for i in  P:
        ok = True
        ng = False
        if i-1 >= 0:
            if seen[i-1]:
                ok = False
        if i+1 < N:
            if seen[i+1]:
                ok = False
        if i-1 >= 0 and i+1 < N and seen[i-1] and seen[i+1]:
            ng = True
        if ok:
            cnt += 1
        if ng:
            cnt -= 1
        seen[i] = 1
    ans = max(ans, cnt)
    prev = cnt
print(ans)


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

N = int(input())
character = [int(input()) for _ in range(N)]

def dfs(l, r):
    if l < 0 and r >= N:
        return 0
    elif l < 0:
        c = character[r]
    else:
        c = character[l]
    li = l
    while li >= 0 and character[li] == c:
        li -= 1
    ri = r
    while ri < N and character[ri] == c:
        ri += 1
    pr = 0
    if l == r:
        pr = 1
    
    if abs(l-li) + abs(r-ri) - pr < 4:
        return l+N-r+1-pr
    return dfs(li, ri)

ans = INF
for i in range(N):
    p = character[i]
    for j in range(1, 4):
        character[i] = j
        ans = min(ans, dfs(i, i))
        character[i] = p
print(ans)

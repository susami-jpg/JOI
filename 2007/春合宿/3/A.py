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

f = [0] * 21
f[1] = 1
for i in range(2, 21):
    f[i] = f[i-1]*i
    
s = list(input())
N = len(s)
rec = [0] *26
for i in range(N):
    s[i] = ord(s[i])-65
    rec[s[i]] += 1

ans = 0
for i in range(N):
    cur = s[i]
    rest = N-i-1
    for j in range(cur):
        c = f[rest]
        if rec[j]:
            rec[j] -= 1
            for k in range(26):
                if rec[k]:
                    c //= f[rec[k]]
            rec[j] += 1
            ans += c
    rec[cur] -= 1
print(ans+1)

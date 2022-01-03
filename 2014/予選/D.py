from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10007

N = int(input())
inp = input()
s = [-1]
for i in range(N):
    if inp[i] == "J":
        s.append(0)
    elif inp[i] == "O":
        s.append(1)
    else:
        s.append(2)
        
dp = [[0] * (1<<3) for _ in range(N+1)]
dp[0][1] = 1
for i in range(N):
    for S in range(1<<3):
        if dp[i][S] == 0:continue
        for nxtS in range(1<<3):
            if nxtS&(1<<s[i+1]) == 0 or nxtS&S == 0:continue
            dp[i+1][nxtS] += dp[i][S]
            dp[i+1][nxtS] %= MOD

ans = 0
for S in range(1<<3):
    ans += dp[N][S]
    ans %= MOD
#for row in dp:
    #print(row)
print(ans)

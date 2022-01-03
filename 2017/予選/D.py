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
MOD = 10**9+7

N, M = map(int, input().split())
#cnt[s]:= s種類目の人形の個数
cnt = [0] * 20
#acc_doll[s]:= s種類目の人形の個数とそのindexを累積和で管理(1-indexed)
acc_doll = [[0] * (N+1) for _ in range(20)]
for i in range(1, N+1):
    s = int(input())
    s -= 1
    cnt[s] += 1
    acc_doll[s][i] += 1

for s in range(20):
    acc_doll[s] = list(accumulate(acc_doll[s]))

#dp[msk]:= mskのbit集合に含まれる種類の人形の並べ方が決まっている状態で、並べ替えるために取り出すぬいぐるみの個数の最小値
dp = [INF] * (1<<M)
dp[0] = 0
for msk in range(1<<M):
    if dp[msk] == INF:continue
    #leftは現在並べ方決定している人形の個数
    left = 0
    for s in range(M):
        if (msk>>s)&1:
            left += cnt[s]
    
    for nxt in range(M):
        if (msk>>nxt)&1:continue
        right = left + cnt[nxt]
        #costは(left, right]の区間で種類sの人形を配置するためにかかるcost
        cost = cnt[nxt] - (acc_doll[nxt][right] - acc_doll[nxt][left])
        dp[msk|(1<<nxt)] = min(dp[msk|(1<<nxt)], dp[msk] + cost)

print(dp[(1<<M)-1])

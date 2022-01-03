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
"""
def popcount(x):
    '''xの立っているビット数をカウントする関数(xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f
"""
def popcount(n):
    return bin(n).count("1")

H, W = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(H)]
mp = [[] for _ in range(3)]
for i in range(H):
    black = 0
    gray = 0
    white = 0
    for j in range(W):
        if field[i][j] == 0:
            black |= 1<<(W-1-j)
        elif field[i][j] == 1:
            gray |= 1<<(W-1-j)
        else:
            white |= 1<<(W-1-j)
    mp[0].append(black)
    mp[1].append(gray)
    mp[2].append(white)

ans = 0
for i in range(H):
    for j in range(W):
        for r in range(i):
            if field[i][j] == field[r][j]:
                n1 = (field[i][j] + 1)%3
                n2 = (field[i][j] + 2)%3
                ans += popcount((mp[n1][i]>>(W-j)) & (mp[n2][r]>>(W-j)))
                ans += popcount((mp[n2][i]>>(W-j)) & (mp[n1][r]>>(W-j)))
            else:
                if (field[i][j] + 1)%3 == field[r][j]:
                    n = (field[i][j] + 2)%3
                else:
                    n = (field[i][j] + 1)%3
                ans += popcount((mp[n][i]>>(W-j)) | (mp[n][r]>>(W-j)))
print(ans)
          


'''
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진
기존방식은 2초를 넘을수밖에 없으므로, 에라토스테네스의 체를 사용하여야 함
'''
import sys

M,N = map(int,sys.stdin.readline().split())

dp = [True]*(N+1)
dp[0]=False
dp[1]=False
for idx in range(2,N+1):
    if dp[idx]:
        if idx>=M:
            print(idx)
        for dp_idx in range(idx*2,N+1,idx):
            dp[dp_idx]=False
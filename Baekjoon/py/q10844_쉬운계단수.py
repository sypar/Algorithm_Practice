'''
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''
import sys
N = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1] = [1 for _ in range(10)]

for y in range(2,N+1):
    for x in range(10):
        if x==0:
            dp[y][x] = dp[y-1][x+1]
        elif x==9:
            dp[y][x] = dp[y-1][x-1]
        else:
            dp[y][x] = dp[y-1][x-1] + dp[y-1][x+1]

print(sum(dp[N][1:])%int(10E8))
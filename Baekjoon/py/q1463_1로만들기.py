'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 10E6보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''
import sys
N = int(sys.stdin.readline().rstrip())
dp = [-1 for _ in range(1000001)]

def cal(n):
    global dp
    if n == 1:
        return 0
    elif dp[n]!=-1:
        return dp[n]
    else:
        if n%6 == 0:
            dp[n] = min(cal(n//3),cal(n//2))+1
        elif n%3 == 0:
            dp[n] = min(cal(n//3),cal(n-1))+1
        elif n%2 == 0:
            dp[n] = min(cal(n//2),cal(n-1))+1
        else :
            dp[n] = cal(n-1)+1
        return dp[n]
print(cal(N))
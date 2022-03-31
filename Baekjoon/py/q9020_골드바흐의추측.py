'''
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다.

하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.

이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.

예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.

10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.

만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

'''

import sys

T = int(sys.stdin.readline().rstrip())

def two_pointer(plist,end,target):
    p_1st = (end//2)+1
    while plist[p_1st]==False:
        p_1st-=1
    p_2nd = p_1st
    while True:
        if p_1st + p_2nd == target:
            print(f'{p_1st} {p_2nd}')
            break
        elif p_2nd<end:
            if p_1st + p_2nd < target:
                p_2nd+=1
                while plist[p_2nd] == False:
                    p_2nd+=1
            else :
                p_1st-=1
                while plist[p_1st] == False:
                    p_1st-=1
                p_2nd=p_1st

dp = [True]*(10001)
dp[0]=False
dp[1]=False
for idx in range(2,100):
    if dp[idx]:
        for dp_idx in range(idx*2,10001,idx):
                dp[dp_idx]=False

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    two_pointer(dp,len(dp)-1,N)
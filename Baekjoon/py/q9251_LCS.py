'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''
import sys
word1 = list(map(str,sys.stdin.readline().rstrip()))
word2 = list(map(str,sys.stdin.readline().rstrip()))
dp = [[ 0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

for id_y in range(1,len(dp)):
    for id_x in range(1,len(dp[0])):
        if word1[id_x-1] == word2[id_y-1]:
            dp[id_y][id_x] = dp[id_y-1][id_x-1] + 1
        elif id_x == 1:
            dp[id_y][id_x] = dp[id_y-1][id_x]
        elif id_y == 1:
            dp[id_y][id_x] = dp[id_y][id_x-1]
        else:
            dp[id_y][id_x] = max(dp[id_y][id_x-1] , dp[id_y-1][id_x])

print(dp[-1][-1])
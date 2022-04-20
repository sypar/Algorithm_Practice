'''
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''
import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

udp = [0 for _ in range(N)]
for c1 in range(N):
    for c2 in range(N):
        if arr[c1]>arr[c2] and udp[c1]<udp[c2]:
            udp[c1]=udp[c2]
    udp[c1]+=1

ldp = [ 0 for _ in range(N)]
for c1 in range(N-1,-1,-1):
    for c2 in range(N-1,-1,-1):
        if arr[c1]>arr[c2] and ldp[c1]<ldp[c2]:
            ldp[c1]=ldp[c2]
    ldp[c1]+=1

max_val = ldp[0]
for idx in range(N):
    if idx==N-1:
        max_val = max(max_val,udp[idx])
    elif arr[idx]>arr[idx+1]:
        max_val = max(max_val,udp[idx]+ldp[idx]-1)
print(max_val)
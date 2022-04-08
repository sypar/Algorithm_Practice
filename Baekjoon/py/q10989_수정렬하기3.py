'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

카운팅 정렬
'''
import sys
T=int(sys.stdin.readline().rstrip())
arr = [ 0 for _ in range(10001)] 
for _ in range(T):
    arr[int(sys.stdin.readline().rstrip())] += 1

for idx in range(10001):
    while arr[idx]!=0:
        print(idx)
        arr[idx]-=1
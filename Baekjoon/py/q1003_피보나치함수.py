'''
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
'''
import sys
T = int(sys.stdin.readline().rstrip())
fibo = [0, 1] + [ 0 for _ in range(39)]
call_0 = [1,0] +[ 0 for _ in range(39)]
call_1 = [0,1] +[ 0 for _ in range(39)]
answer = []
def fibonacci(n) :
    global fibo, call_0,call_1
    if n == 0 :
        return fibo[0]
    elif n == 1:
        return fibo[1]
    elif fibo[n]==0:
        fibo[n] = fibonacci(n-1) + fibonacci(n-2)
        if call_0[n] == 0:
            call_0[n] = call_0[n-1]+call_0[n-2]
            call_1[n] = call_1[n-1]+call_1[n-2]
        return fibo[n]
    else : 
        return fibo[n]

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    fibonacci(n)
    answer.append([call_0[n], call_1[n]])

for idx in range(len(answer)):
    print(f'{answer[idx][0]} {answer[idx][1]}')
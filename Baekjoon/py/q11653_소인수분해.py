'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''
import sys,math

N = int(sys.stdin.readline().rstrip())
deci_list = [2,3,5] #default
idx = 0

def find_deci():
    global deci_list
    tmp_v = deci_list[-1]
    while True:
        tmp_v+=1
        for dec in range(2,math.floor(math.sqrt(tmp_v))+1):
            if tmp_v%dec == 0:
                break
            elif dec==math.floor(math.sqrt(tmp_v)):
                deci_list.append(tmp_v)
        if tmp_v == deci_list[-1]:
            break
           
while N!=1:
    N,remain = divmod(N,deci_list[idx])
    if remain == 0:
        print(deci_list[idx])
        continue
    elif remain !=0 :
        N=N*deci_list[idx]+remain
        remain = 0
        idx+=1
        if idx==len(deci_list)-1:
            find_deci()
    else :
        break
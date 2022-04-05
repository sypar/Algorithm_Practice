'''
666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다.

조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고,

피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.

하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.

종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.

따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.

일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
0 < N <= 10,000
'''
import sys

N = int(sys.stdin.readline().rstrip())
idx = 2
val = 1
n = val
if N==1:
    print('666')
else:
    while idx<=N:
        str_n = str(n)
        po_ = 1
        for i in range(len(str_n)-1,0,-1):
            if str_n[i]==str_n[i-1] and str_n[i]=='6':
                po_+=1
            else:
                break
        if val == 6:
            left = ''
            if str_n[0]=='6' and n<10:
                left = ''
            else:
                length = len(str_n)
                while length>0:
                    if str_n[length-1]=='6':
                        length-=1
                    else:
                        break
                for i in range(length):
                    left += str_n[i]
            for i in range(10**po_):
                series = left +'666' + '0'*(po_- len(str(i))) + str(i)
#                print(f'{idx}번쨰 : {series}')
                idx+=1
                if idx>N:
                    break
            val +=1
        else :
            series = str_n+'666'
#            print(f'{idx}번쨰 : {series}')
            idx+=1
            val+=1
            if val==16:
                val-=10       
        n+=1
    print(series)

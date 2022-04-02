'''
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

'''
import sys
N = int(sys.stdin.readline().rstrip())
data=[ ['*' for _ in range(N)] for _ in range(N) ]  # NXN 정사각형

def star(n):    # N 27 / 
    off_x=0
    off_y=0
    while off_y<N:
        for idx_x in range((n//3),2*(n//3)):
            for idx_y in range((n//3),2*(n//3)):
                if data[off_x+idx_x][off_y+idx_y]=='*':
                    data[off_x+idx_x][off_y+idx_y]=' '
        if off_x <= N:
            off_x += n
        if off_x >= N:
            off_x = 0
            off_y += n
    if n<N:
        star(n*3)
star(3)
for idx_x in range(N):
    for idx_y in range(N):
        print(data[idx_x][idx_y],end='')
    print(end='\n')

    """
    Best
    
    def printStar(n):
    if n == 1:
        return "*"
    else:
        prev = printStar(n/3).split("\n")
        result = ""
        for i in prev:
            result += i * 3 + "\n"
        for i in prev:
            result += i + i.replace("*", " ") + i + "\n"
        for i in prev: 
            result += i * 3 + "\n"
        return result[:-1]
        
     
N = int(input())

print(printStar(N))

"""
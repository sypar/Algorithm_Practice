'''
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
'''
import sys
while True:
    line = list(map(int,sys.stdin.readline().split()))
    if line == [0,0,0]:
        break
    else:
        line.sort()
        if line[2]**2 == line[1]**2 + line[0]**2 :
            print("right")
        else :
            print("wrong")
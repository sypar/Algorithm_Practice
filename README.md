# Algorithm_Practice
Algorithm Practice for Baekjoon, Programmers, using Python,C++

코테 기법 종류

1. 그리디/구현

2. DFS/BFS : 큐,스택 활용, 최단경로, 영역

3. 정렬 : 선택정렬, 삽입정렬, 퀵정렬, 계수정렬

4. 이진탐색 
    - 순차탐색 : 데이터를 앞부터 하나씩 탐색
    - 이진탐색 : 정렬된 데이터를 시작,중간,끝으로 나눠 탐색
        py : bisect_left, right
        c++ : lower_bound,upper_bound

5. 다이나믹프로그래밍
    - Memozation 기법을 사용하여, 연산량을 조절하는 기법
    Memory를 많이써서 연산량을 줄이거나 
                    or
    Memory를 적게써서 연산량을 늘이거나
    Memorzation 상향식, 하향식으로 구성.
    최적 부분구조, 중복되는문제 인 경우 사용함

    - 분할정복 과의 차이점은 부분 문제의 중복 유무(분할정복에서는 부분 문제가 반복되지 않음)

6. 최단경로문제
    py : heapq 사용
    c++ : priority_queue 사용
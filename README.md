# Algorithm_Practice
Algorithm Practice for Baekjoon, Programmers, using Python,C++

    코테 기법 종류

    1. 그리디/구현

    2. DFS/BFS : 큐,스택 활용, 최단경로, 영역

    3. 정렬 : 선택정렬, 삽입정렬, 퀵정렬, 계수정렬
        Stable Sort
        list=[1, 7(1), 3, 5, 4, 7(2), 9 ]

        이 리스트를 정렬했을 때
        (1) list=[1, 3, 4, 5, 7(1), 7(2), 9
        (2) list=[1, 3, 4, 5, 7(2), 7(1), 9

        (1)처럼 나오면 안정(Stable) 정렬, (2)처럼 나오면 불안정(Unstable) 정렬이라고 한다.

        즉, 정렬을 했을 때 중복된 값들의 순서가 변하지 않으면 안정(Stable) 정렬, 변하면 불안정(Unstable) 정렬인 것이다.

        대표적인 알고리즘들
        Stable Sorting 알고리즘은 다음과 같다:          Unstable Soring 알고리즘:
        Insertion Sort                                  Selection sort
        Merge Sort                                      Heap Sort
        Bubble Sort                                     Shell Sort
        Counting Sort                                   Quick Sort

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

        *LIS 알고리즘
        최장 증가 부분 수열(LIS, Longest Increasing Subsequence)란?
        원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중, 각 원소가 이전 원소보다 크다는 조건을 만족하고, 그 길이가 최대인 부분 수열을 최장 증가 부분 수열이라고 합니다.
        *LCS 알고리즘
        최장 공통 부분 수열(Longest Common Subsequence)

    6. 최단경로문제
        py : heapq 사용
        c++ : priority_queue 사용
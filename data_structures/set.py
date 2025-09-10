"""
[자료구조] 집합 (Set)

- 중복 제거
- 빠른 탐색 (평균 O(1))
"""

def set_example():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("합집합:", a | b)
    print("교집합:", a & b)
    print("차집합:", a - b)

    a.add(7)
    a.discard(2)

    print("2 제거 후 a: ", a)
    print("5 포함 여부: ", 5 in a)


if __name__ == '__main__':
    set_example()
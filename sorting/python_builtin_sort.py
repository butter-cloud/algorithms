"""
[정렬] 파이썬 내장 정렬 함수
- sorted(): 정렬된 새로운 리스트 반환 (원본 유지)
- list.sort(): 리스트 자체를 정렬 (in-place)
- key 매개변수: 정렬 기준 설정
- reverse=True: 내림차순 정렬
"""

def basic_sorted_example():
    data = [5, 2, 9, 1, 7]
    print("원본:", data)

    sorted_data = sorted(data)
    print("오름차순 정렬: ", sorted_data)

    sorted_desc = sorted(data, reverse=True)
    print("내림차순 정렬: ", sorted_desc)

    print("원본 유지됨: ", data)


def in_place_sort_example():
    data = [3, 1, 4, 2]
    print("원본:", data)

    data.sort()
    print("정렬 후: ", data)


def key_example():
    fruits = ['banana', 'apple', 'cherry', 'blueberry']
    print("원본:", fruits)

    # 길이순 정렬
    sorted_by_length = sorted(fruits, key=len)
    print("sorted by length: ", sorted_by_length)

    # 알파벳 역순
    sorted_reverse = sorted(fruits, reverse=True)
    print("sorted reverse: ", sorted_reverse)


if __name__ == "__main__":
    print("\n📌 기본 sorted 사용")
    basic_sorted_example()

    print("\n📌 in-place sort 사용")
    in_place_sort_example()

    print("\n📌 key 정렬 기준 사용")
    key_example()


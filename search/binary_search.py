"""
[탐색] 이진 탐색 (Binary Search)

- 정렬된 배열에서 탐색 범위를 반씩 줄이며 target을 찾는 알고리즘
- 시간복잡도: O(log n)
- 구현 방식:
    - 반복문 (iterative)
    - 재귀 (recursive)
- 입력 배열은 오름차순 정렬되어 있어야 함
"""

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # not found


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1   # not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    print("📍 반복형 결과: ", binary_search_iterative(arr, target))
    print("📍 재귀형 결과: ", binary_search_recursive(arr, target, 0, len(arr)-1))

    print("❌ Not found (Iterative):", binary_search_iterative(arr, 4))  # -1
    print("❌ Not found (Recursive):", binary_search_recursive(arr, 4, 0, len(arr) - 1))  # -1
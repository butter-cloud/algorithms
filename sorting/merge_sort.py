"""
[정렬] 병합 정렬 (Merge Sort)
- 시간복잡도: O(n log n)
- 안정 정렬 (Stable Sort)
- 분할 정복 (Divide and Conquer) 전략 사용
    1. 리스트를 반으로 나눔 (Divide)
    2. 각각 정렬 (재귀 호출)
    3. 두 리스트 병합 (Conquer)
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. 리스트를 반으로 나눔
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # 왼쪽 정렬
    right = merge_sort(arr[mid:])    # 오른쪽 정렬

    # 2. 정렬된 두 리스트 병합
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # 왼쪽과 오른쪽 리스트를 비교하여 작은 값을 먼저 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [8, 4, 2, 9, 1, 5]
    print("Before:", data)
    sorted_data = merge_sort(data)
    print("After:", sorted_data)
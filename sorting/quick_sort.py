"""
[정렬] 퀵 정렬 (Quick Sort)
- 시간복잡도: 평균 O(n log n), 최악 O(n^2)
- 불안정 정렬 (Unstable Sort)
- 분할 정복 (Divide and Conquer)
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]      # 기준값: 첫 번째 요소. 그냥 아무거나 잡은거임!
    tail = arr[1:]      # pivot 제외한 나머지

    # 피벗보다 작거나 같은 값 / 큰 값으로 분리
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    data = [7, 3, 9, 1, 5, 2]
    print("Before:", data)
    sorted_data = quick_sort(data)
    print("After:", sorted_data)
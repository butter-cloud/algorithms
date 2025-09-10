"""
[정렬] 선택 정렬 (Selection Sort)

- 정렬되지 않은 부분에서 가장 작은 (또는 큰) 값을 찾아 맨 앞과 교환하는 방식
- 반복할수록 앞쪽부터 정렬되어 나감

🧠 시간복잡도: O(n^2)
🧠 공간복잡도: O(1)
🧠 특징: 구현은 쉬우나 성능은 떨어짐 (실무에서 거의 안 씀)
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 현재 위치(i) 이후 중 가장 작은 값의 인덱스 찾기
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 가장 작은 값과 현재 위치 값 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == '__main__':
    data = [64, 25, 10, 22, 11]
    print("정렬 전:", data)
    sorted_data = selection_sort(data)
    print("정렬 후:", sorted_data)
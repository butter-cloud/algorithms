"""
[정렬] 버블 정렬 (Bubble Sort)
- 인접한 두 값을 비교해서 큰 값을 뒤로 보내는 방식
- 한 번의 패스(pass)마다 가장 큰 값이 맨 뒤로 이동

🧠 시간복잡도: O(n^2)
🧠 공간복잡도: O(1)
🧠 특징: 구현은 아주 쉬우나 성능이 매우 안 좋음 (실무에서 사용 거의 안 함)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 이미 정렬된 상태인지 확인하는 플래그
        swapped = False
        # 마지막 i개는 이미 정렬되어 있으므로 제외. (가장 큰 값을 뒤로 보냈음)
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 값 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 한 번도 교환이 일어나지 않았다면 이미 정렬된 상태
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8]
    print("정렬 전:", data)
    sorted_data = bubble_sort(data)
    print("정렬 후:", sorted_data)


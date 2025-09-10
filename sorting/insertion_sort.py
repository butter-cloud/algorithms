"""
[정렬] 삽입 정렬 (Insertion Sort)
- 정렬된 부분을 점차 확장해가며 적절한 위치에 '삽입'
- 두 번째 원소부터 시작해서, 앞의 정렬된 부분과 비교하여 적절한 위치에 삽입
- 평균/최악 시간복잡도: O(n²)
- 거의 정렬된 경우 효율적: 최선 O(n)
- in-place 정렬, 안정 정렬
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # 현재 비교 대상
        j = i - 1

        # key보다 큰 값이 왼쪽에 있으면 오른쪽으로 밀기
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]     # 한 칸씩 오른쪽으로 밀어냄
            j -= 1                  # 더 왼쪽으로 이동하며 비교

        arr[j + 1] = key            # while문이 끝나고 빈 자리에 key 삽입

if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    print("Before:", data)
    insertion_sort(data)
    print("After:", data)
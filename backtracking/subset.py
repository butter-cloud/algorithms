"""
[백트래킹] 부분 집합 (Subsets)
- 주어진 집합에서 가능한 모든 부분 집합을 구하는 문제
- 원소를 선택하거나 선택하지 않는 두 가지 경우로 가지를 나눔
- 백트래킹(backtracking) 또는 DFS로 구현 가능
- 총 부분집합의 수는 2^n개 (n: 원소 개수)

예)
nums = [1, 2, 3]일 때 출력:
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
"""

def subsets(nums):
    result = []

    def backtrack(index, path):
        # 현재까지 만든 부분 집합을 저장
        result.append(path[:])

        # 현재 index 부터 끝까지 모든 경우 탐색
        # index == len(nums)가 되면 빈 range가 되서 for 루프가 실행되지 않음
        for i in range(index, len(nums)):
            path.append(nums[i])    # 원소 추가
            backtrack(i + 1, path)  # 다음 index로 재귀 호출
            path.pop()              # backtracking: 선택 취소

    backtrack(0, [])
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    all_subsets = subsets(nums)
    for s in all_subsets:
        print(s)
"""
[백트래킹] 조합 (Combinations)
- 1부터 n까지의 숫자 중에서 m개를 고르는 모든 조합을 구하는 문제
- 순서를 고려하지 않음 (1,2 와 2,1은 같은 조합으로 취급)
- 중복 없이 각 숫자를 한 번씩만 사용
- 백트래킹(backtracking)으로 구현. 조건이 맞지 않으면 되돌아가기
"""

def combine(n, m):
    result = []

    def backtrack(start, path):
        # m개를 다 골랐으면 저장
        if len(path) == m:
            result.append(path[:])  # 복사해서 저장
            return

        # start 부터 n까지 숫자 선택
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)      # 이때 i는 빼고 넘기므로 중복되지 않고 고를 수 있음
            path.pop()

    backtrack(1, [])
    return result


if __name__ == "__main__":
    combos = combine(4, 2)
    for c in combos:
        print(c)
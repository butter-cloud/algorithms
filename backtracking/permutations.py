"""
[백트래킹] 순열 (Permutations)
- 1부터 n까지의 숫자 중에서 순서를 고려해 모든 조합을 구하는 문제
- 중복 없이 각 숫자를 한 번씩만 사용
- 백트래킹(backtracking)으로 구현: 조건이 맞지 않으면 되돌아가기

예)
n = 3일 때 출력:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""

def backtrack(path, used, n):
    # 종료 조건: path의 길이가 n이면 하나의 순열 완성. 종료.
    # return이 되면 path와 used 원상복귀
    if len(path) == n:
        print(path)
        return

    # 1부터 n까지 숫자를 시도
    for i in range(1, n + 1):
        # 이미 사용한 숫자는 건너뛰기
        # 한 조합 내에서 숫자는 중복되지 않아야 함
        if i in used:
            continue

        # 선택한 숫자를 path에 추가하고 사용 처리
        path.append(i)
        used.add(i)

        # 다음 위치에 대해 재귀 호출
        backtrack(path, used, n)

        # 백트래킹 (되돌리기): 마지막 숫자 제거 + 사용 취소
        path.pop()
        used.remove(i)




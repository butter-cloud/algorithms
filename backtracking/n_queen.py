"""
[백트래킹] N-Queen 문제
- N x N 체스판에 N개의 퀸을 서로 공격하지 않도록 배치
- 퀸은 같은 행(row, 가로방향), 열(col, 세로방향), 대각선에 함께 있을 수 없음. (그렇게 있으면 서로 공격하는 거임)
- 백트래킹을 통해 가능한 모든 경우 탐색
"""

def solve_n_queens(n):
    result = []
    board = []

    def is_valid(row, col):
        for r in range(row):
            # 같은 열 or 대각선 상에 퀸에 있는지 확인
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        # n번째 행까지 갔을 경우 하나의 답 완성
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_valid(row, col):
                board.append(col)
                backtrack(row + 1)      # 다음 행으로
                board.pop()

    backtrack(0)    # 0행부터 시작
    return result


def print_board(result, n):
    """해답 리스트를 체스판 형태로 출력"""
    for sol in result:
        for i in range(n):
            row = ['.'] * n
            row[sol[i]] = 'Q'
            print(''.join(row))
        print()


if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"{n}-Queen 해답 개수:", len(solutions))
    print_board(solutions, n)
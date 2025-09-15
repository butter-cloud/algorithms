"""
[시뮬레이션 문제] 로봇 청소기
- N x M 크기의 방에서 로봇이 청소를 수행
- 1: 벽, 0: 청소 가능한 공간
- 로봇은 아래 조건대로 작동:

1. 현재 위치를 청소한다
2. 왼쪽 방향부터 차례대로 주변 4칸을 탐색한다
    - 청소되지 않은 칸이 있으면 왼쪽으로 회전 후 한 칸 전진
    - 없다면 방향 유지하고 한 칸 후진. 후진도 불가하면 작동 종료
3. 청소한 칸의 수를 출력한다

[방향 정의]
0: 북, 1: 동, 2: 남, 3: 서
"""

# 방향 벡터 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d):
    """왼쪽으로 회전 (반시계 방향)"""
    return (d + 3) % 4

def simulate_cleaning(n, m, x, y, d, room):
    cleaned = [[0] * m for _ in range(n)]
    count = 0

    while True:
        # 1. 현재 위치 청소
        if cleaned[x][y] == 0:
            cleaned[x][y] = 1
            count += 1

        moved = False
        for _ in range(4):
            d = turn_left(d)
            # turn_left에서 방향 계산 후 그 방향으로 한 칸 이동한 위치가 nx, ny
            nx, ny = x + dx[d], y + dy[d]
            # 벽이 아니고 아직 청소 안된 공간이면
            if room[nx][ny] == 0 and cleaned[nx][ny] == 0:
                x, y = nx, ny
                moved = True
                break

        if not moved:
            # 후진
            back_x, back_y = x - dx[d], y - dy[d]
            # 후진했을 때 벽이면 break
            if room[back_x][back_y] == 1:
                break
            else:
                x, y = back_x, back_y

    return count


if __name__ == "__main__":
    # 입력 예시
    N, M = 3, 3
    room = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    x, y, d = 1, 1, 0  # 시작 위치와 방향 (북쪽)

    result = simulate_cleaning(N, M, x, y, d, room)
    print("청소한 칸 수:", result)
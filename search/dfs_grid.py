"""
[탐색] DFS (2차원 배열)

- 격자형 지도에서 연결된 땅(1)을 하나의 섬으로 보고 탐색
- 상하좌우 방향으로 이동
"""

def dfs(grid, x, y, visited):
    # n이 세로, m이 가로
    n, m = len(grid), len(grid[0])

    # 범위를 벗어나면 바로 return
    if x < 0 or x >=n or y < 0 or y >= m:
        return
    # 1(땅 부분)만 탐색하기로 했으니까
    if grid[x][y] == 0 or visited[x][y]:
        return

    visited[x][y] = True

    # 상하좌우 방향 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(grid, nx, ny, visited)


if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ]

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    print("DFS로 (0,0)부터 탐색: ")
    dfs(grid, 0, 0, visited)

    print("방문 결과: ")
    for row in visited:
        print(row)


def count_islands(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(grid, i, j, visited)
                print(f"새 섬 발견 at ({i}, {j})")
                count += 1
    return count


if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0]
    ]

    print("섬의 개수:", count_islands(grid))  # 출력: 2

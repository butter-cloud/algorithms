"""
[탐색] 깊이 우선 탐색 (DFS, Depth First Search)

- 그래프에서 가능한 한 깊게 탐색한 후, 더 이상 갈 곳이 없으면 백트래킹
- 구현 방식:
    - 재귀
    - 스택 사용 (비재귀)
- 방문 처리 필요: 무한 루프 방지
"""

def dfs(graph, start, visited=None):
    """
    재귀로 구현한 DFS
    :param graph: 인접 리스트 형식의 그래프
    :param start: 시작 노드
    :param visited: 방문한 노드 기록용 집합
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end= ' ')  # 방문 노드 출력

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


if __name__ == '__main__':
    # 예시 그래프 (무방향, 연결 그래프)
    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    print("A에서 시작한 DFS 탐색 결과:")
    dfs(graph, 'A')
from collections import deque

"""
[탐색] 너비 우선 탐색 (BFS, Breadth First Search)
"""

def bfs(graph, start):
    """
    큐를 사용한 BFS
    :param graph: 인접 리스트 형식의 그래프
    :param start: 시작 노드
    """

    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ') # 방문 노드 출력

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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

    print("A에서 시작한 BFS 탐색 결과:")
    bfs(graph, 'A')
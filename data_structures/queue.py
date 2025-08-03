"""
[자료구조] 큐 (Queue)

- 선입선출(FIFO, First In First Out)
- 주요 연산:
    - enqueue: 데이터 삽입
    - dequeue: 앞의 데이터 제거 및 반환
    - peek: 가장 앞 데이터 조회
    - is_empty: 비었는지 확인
    - size: 현재 큐 크기
- python에서는 collections.deque 로 구현
"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue error: queue is empty')
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError('peek error: queue is empty')
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()

    print("큐가 비었나요?", q.is_empty())  # True

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print("큐 크기:", q.size())  # 3
    print("맨 앞:", q.peek())  # A
    print("dequeue:", q.dequeue())  # A
    print("dequeue:", q.dequeue())  # B
    print("큐가 비었나요?", q.is_empty())  # False
    print("dequeue:", q.dequeue())  # C
    print("큐가 비었나요?", q.is_empty())  # True

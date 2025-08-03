"""
[자료구조] 스택 (Stack)

- 후입선출 (LIFO, Last In First Out)
- 주요 연산:
    - push: 데이터 삽입
    - pop: 마지막 데이터 제거
    - peek: 가장 위의 데이터 조회
    - is_empty: 비었는지 확인
    - size: 현재 스택 크기
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        """ 가장 위의 항목 제거 및 반환 """
        if self.is_empty():
            raise IndexError('Pop Error: Stack is empty')
        return self.items.pop()

    def peek(self):
        """ 가장 위의 항목 반환 (제거하지는 않음) """
        if self.is_empty():
            raise IndexError('Peek Error: Stack is empty')
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    print("스택이 비었나요?", stack.is_empty())  # True

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("현재 스택 크기:", stack.size())      # 3
    print("가장 위 원소:", stack.peek())        # 30

    print("pop:", stack.pop())                  # 30
    print("pop:", stack.pop())                  # 20
    print("스택이 비었나요?", stack.is_empty())  # False
    print("pop:", stack.pop())                  # 10
    print("스택이 비었나요?", stack.is_empty())  # True
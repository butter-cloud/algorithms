"""
[재귀] Recursion
- 함수가 자기 자신을 호출하는 방식
- 종료 조건 (base case) 이 반드시 필요함
- 대표 예시: 팩토리얼, 피보나치 수열, 리스트 누적합 등
"""

def factorial(n):
    """팩토리얼: n! = n * (n-1)!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """피보나치: F(n) = F(n-1) + F(n-2)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_list(arr, idx=0):
    if idx == len(arr):
        return 0
    return arr[idx] + sum_list(arr, idx + 1)
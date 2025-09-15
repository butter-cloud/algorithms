"""
[완전탐색] 1부터 N까지 자연수 중 3개를 골라 합이 M이 되는 경우의 수
- itertools.combinations 활용

조건:
- 중복 없이 서로 다른 3개의 수
- 순서 상관 없음
- 모든 조합을 검사 (Brute-force)
"""

from itertools import combinations

def count_combinations(n, m):
    count = 0
    for comb in combinations(range(1, n + 1), 3):
        if sum(comb) == m:
            print(f"유효한 조합입니다: {comb}")
            count += 1
    return count


if __name__ == "__main__":
    N = 5
    M = 6
    result = count_combinations(N, M)
    print(f"{N}까지 자연수 중 3개의 합이 {M}이 되는 조합 수: {result}")
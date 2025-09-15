"""
[완전탐색] 1부터 N까지 자연수 중 3개를 골라 합이 M이 되는 경우의 수

예)
N = 5, M = 6 일 때 가능한 조합:
- (1, 2, 3)

조건:
- 중복 없이 서로 다른 3개의 수
- 순서 상관 없음
- 모든 조합을 검사 (Brute-force)
"""

def count_combinations(n, m):
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == m:
                    print(f"유효한 조합 발견! - ({i}, {j}, {k})")
                    count += 1
    return count


if __name__ == "__main__":
    N = 5
    M = 6
    result = count_combinations(N, M)
    print(f"{N}까지 자연수 중 3개의 합이 {M}이 되는 조합 수: {result}")
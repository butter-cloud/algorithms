"""
 [자료구조] 해시(Hash)

 - Key를 해시 함수를 통해 Index로 변환
 - Dictionary나 Set이 내부적으로 Hash 기반
"""

def two_sum(nums, target):
    """
    LeetCode 스타일 문제: Two Sum

    정수 배열 nums와 정수 target이 주어졌을 때,
    합이 target이 되는 두 수의 인덱스를 찾아라.

    주어진 배열에서 합이 target이 되는 두 수의 인덱스를 반환
    - 시간복잡도: O(n)
    - 해시맵을 이용해 현재 숫자의 '짝(complement)'을 찾는 방식

    Parameters:
    - nums: List[int] – 숫자 리스트
    - target: int – 원하는 합

    Returns:
    - List[int] – 조건을 만족하는 두 수의 인덱스
    """
    num_map = {}    # {숫자: 인덱스}

    for i, num in enumerate(nums):
        complement = target - num   # 현재 숫자와 더했을 때 target이 되는 '짝'

        # complement 가 이미 num_map에 있다는 것은 이미 답을 찾았다는 것
        # complement 의 index를 알고 있으므로 바로 답을 반환하면 됨!
        if complement in num_map:
            return [num_map[complement], i]

        # 없으면 현재 인덱스를 해시맵에 저장
        num_map[num] = i

    # 문제 조건상 항상 해답이 존재하므로 여긴 안 올 예정
    return []
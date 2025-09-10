"""
[자료구조] 딕셔너리 (Dictionary / HashMap)

- Key–Value 쌍으로 구성
- 평균 시간 복잡도: O(1)
- 중복된 Key 불가
"""

def dict_example():
    student_scores = {
        'Alice': 95,
        'Bob': 88,
        'Charlie': 72
    }

    # 조회
    print(student_scores['Alice'])

    # 수정
    student_scores['Bob'] = 90

    # 추가
    student_scores['David'] = 85

    # 존재 여부 확인
    if 'Charlie' in student_scores:
        print('Charlie exists')

    # 전체 순회
    for name, score in student_scores.items():
        print(f'{name}: {score}')

if __name__ == '__main__':
    dict_example()
# [숫자로 이루어진 사각형 ](https://www.codetree.ai/missions/5/problems/rectangle-with-a-number)

|유형|문제 경험치|난이도|
|---|---|---|
|[Novice Mid / 함수 / 값을 반환하지 않는 함수](https://www.codetree.ai/missions?missionId=5)|10xp|![쉬움][easy]|


## 🕰️ 복잡도 알아보기

```python
def n_by_n_rect(n):
    i = 1
    for _ in range(n):
        for _ in range(n):
            print(i, end=' ')
            i += 1
            if i==10:
                i = 1
        print()
    
n = int(input())
n_by_n_rect(n)
```

### 시간 복잡도 (Time Complexity)
코드에서 두 개의 중첩된 루프가 있으며, 각 루프는 n번씩 실행된다.
내부 루프 안의 모든 작업은 상수 시간 O(1)에 수행된다.

- 외부 루프: n번 반복
- 내부 루프: n번 반복 
- 내부 루프의 작업: 상수 시간 O(1)

따라서 총 시간 복잡도는 O(n) * O(n) = O(n^2) 이다. <br>

### 공간 복잡도 (Space Complexity)
이 코드에서 추가로 사용하는 메모리는 주로 변수 i와 두 개의 루프 인덱스이다. 이 변수들은 모두 상수 개수이고, 반복 횟수에 상관없이 일정한 메모리만 사용한다.

- i: 상수 공간 O(1)
- 두 개의 루프 인덱스: 상수 공간 O(1)

따라서 이 코드의 공간 복잡도는 O(1) 이다.

### 요약
- 시간 복잡도: O(n^2)
- 공간 복잡도: O(1)





[b5]: https://img.shields.io/badge/Bronze_5-%235D3E31.svg
[b4]: https://img.shields.io/badge/Bronze_4-%235D3E31.svg
[b3]: https://img.shields.io/badge/Bronze_3-%235D3E31.svg
[b2]: https://img.shields.io/badge/Bronze_2-%235D3E31.svg
[b1]: https://img.shields.io/badge/Bronze_1-%235D3E31.svg
[s5]: https://img.shields.io/badge/Silver_5-%23394960.svg
[s4]: https://img.shields.io/badge/Silver_4-%23394960.svg
[s3]: https://img.shields.io/badge/Silver_3-%23394960.svg
[s2]: https://img.shields.io/badge/Silver_2-%23394960.svg
[s1]: https://img.shields.io/badge/Silver_1-%23394960.svg
[g5]: https://img.shields.io/badge/Gold_5-%23FFC433.svg
[g4]: https://img.shields.io/badge/Gold_4-%23FFC433.svg
[g3]: https://img.shields.io/badge/Gold_3-%23FFC433.svg
[g2]: https://img.shields.io/badge/Gold_2-%23FFC433.svg
[g1]: https://img.shields.io/badge/Gold_1-%23FFC433.svg
[p5]: https://img.shields.io/badge/Platinum_5-%2376DDD8.svg
[p4]: https://img.shields.io/badge/Platinum_4-%2376DDD8.svg
[p3]: https://img.shields.io/badge/Platinum_3-%2376DDD8.svg
[p2]: https://img.shields.io/badge/Platinum_2-%2376DDD8.svg
[p1]: https://img.shields.io/badge/Platinum_1-%2376DDD8.svg
[passed]: https://img.shields.io/badge/Passed-%23009D27.svg
[failed]: https://img.shields.io/badge/Failed-%23D24D57.svg
[easy]: https://img.shields.io/badge/쉬움-%235cb85c.svg?for-the-badge
[medium]: https://img.shields.io/badge/보통-%23FFC433.svg?for-the-badge
[hard]: https://img.shields.io/badge/어려움-%23D24D57.svg?for-the-badge
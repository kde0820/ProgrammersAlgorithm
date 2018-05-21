def bestSet(n, s):
    if s//n == 0:
        return [-1]
    answer = [s//n for i in range(n)]
    remain = s % n
    index = -1
    while remain > 0:
        answer[index] += 1
        remain -= 1
        index -= 1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(bestSet(3,13))
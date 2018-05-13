def Harshad(n):
    # n은 하샤드 수 인가요?
    digit_sum = 0
    for i in str(n):
        digit_sum += int(i)
    return True if n % digit_sum == 0 else False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
def sumDivisor(num):
    answer = 1
    for i in range(2,num+1):
        if num % i == 0:
            answer += i
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
def nlcm(num):
    answer = num[0]
    for i in range(1, len(num)):
        answer = answer * num[i] / gcd(answer, num[i])
    return int(answer)

def gcd(a, b):
    while b != 0:
        r = a%b
        a, b = b, r
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]))
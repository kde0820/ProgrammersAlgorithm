def gcdlcm(a, b):
    m = a
    n = b
    while True:
        r = m % n
        if r == 0:
            gcd = n
            break
        else:
            m = n
            n = r
    lcm = int(a * b / gcd)
    answer = [gcd, lcm]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))
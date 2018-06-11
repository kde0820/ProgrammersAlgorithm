import math
def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    no_prime = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if i not in no_prime:
            for j in range(i+1, n+1):
                if j not in no_prime:
                    if j % i == 0:
                        no_prime.append(j)
    return n - len(no_prime)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
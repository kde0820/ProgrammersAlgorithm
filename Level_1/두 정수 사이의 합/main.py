def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a, b), max(a, b)+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
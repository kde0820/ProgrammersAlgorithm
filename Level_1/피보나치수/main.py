dic = {0:0, 1:1}
def fibonacci(num):
    if num in dic:
        return dic[num]
    dic[num] = fibonacci(num-1) + fibonacci(num-2)
    return dic[num]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
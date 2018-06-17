# -*- coding: utf-8 -*-
def expressions(num):
    answer = 1
    for i in range(num - 1, 1, -1):
        print("i: ", i)
        j = i
        n = num
        while j - 1 > 0 and (n - j) >= (j - 1):
            n -= j
            j -= 1
            if n - j == 0:
                answer += 1
                break 
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15))

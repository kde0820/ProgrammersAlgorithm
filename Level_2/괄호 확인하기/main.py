def is_pair(s):
    # 함수를 완성하세요
    result = False
    s_list = []
    for char in s:
        if char == '(':
            s_list.append('(')
        elif char == ')':
            if len(s_list) == 0:
                return False
            s_list.remove('(')
            result = True
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
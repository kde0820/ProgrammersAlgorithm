def string_middle(str):
    # 함수를 완성하세요
    length = len(str)
    index = length // 2
    if length % 2 == 0:
        return str[index-1:index+1]
    return str[index]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
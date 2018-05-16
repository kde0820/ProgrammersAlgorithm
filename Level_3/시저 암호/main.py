def caesar(s, n):
    # 주어진 문장을 암호화하여 반환하세요.
    char_list = list(s)
    for i in range(len(char_list)):
        char = char_list[i]
        if char == " ":
            continue
        asc = ord(char)
        if char.islower():
            asc = (asc + n) - 97
            if asc > 25:
                asc = asc % 26
            char_list[i] = chr(asc + 97)
        else:
            asc = (asc + n) - 65
            if asc > 25:
                asc = asc % 26
            char_list[i] = chr(asc + 65)      
    return "".join(char_list)
    
# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
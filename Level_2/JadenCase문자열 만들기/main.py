def Jaden_Case(s):
    # 함수를 완성하세요
    s_list = s.lower().split()
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    return " ".join(s_list)       
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
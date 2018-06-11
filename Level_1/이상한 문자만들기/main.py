def toWeirdCase(s):
    # 함수를 완성하세요
    word_list = s.lower().split()
    for word_idx in range(len(word_list)):
        for i in range(len(word_list[word_idx])):
            if i % 2 == 0:
                word_list[word_idx] = word_list[word_idx][:i] + word_list[word_idx][i].upper() + word_list[word_idx][i+1:]
    return ' '.join(word_list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));
def solution(s):
    s_list = s.lower().split(' ')
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    return " ".join(s_list)
def solution(phone_number):
    str_list = list(phone_number)
    #함수를 완성해 별이를 도와주세요
    for i in range(len(phone_number)-4):
        str_list[i] = '*'
    return "".join(str_list)
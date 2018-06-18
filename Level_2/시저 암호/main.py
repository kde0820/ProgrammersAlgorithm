def solution(s, n):
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
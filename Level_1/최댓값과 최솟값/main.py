def solution(s):
    result = []
    num_list = [int(n) for n in s.split()]
    result.append(str(min(num_list)))
    result.append(str(max(num_list)))
    return ' '.join(result)
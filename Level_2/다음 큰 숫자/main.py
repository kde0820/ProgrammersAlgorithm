def solution(n):
    one_count = bin(n).count('1')
    n += 1
    while bin(n).count('1') != one_count:
        n += 1
    return n
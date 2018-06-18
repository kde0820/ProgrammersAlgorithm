def solution(n):
    answer = 1
    for i in range(n - 1, 1, -1):
        j = i
        num = n
        while j - 1 > 0 and (num - j) >= (j - 1):
            num -= j
            j -= 1
            if num - j == 0:
                answer += 1
                break 
    return answer
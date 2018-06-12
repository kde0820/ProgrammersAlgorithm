def solution(x):
    digit_sum = 0
    for i in str(x):
        digit_sum += int(i)
    return True if x % digit_sum == 0 else False
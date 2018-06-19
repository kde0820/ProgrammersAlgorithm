def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = answer * arr[i] / gcd(answer, arr[i])
    return int(answer)

def gcd(a, b):
    while b != 0:
        r = a%b
        a, b = b, r
    return a
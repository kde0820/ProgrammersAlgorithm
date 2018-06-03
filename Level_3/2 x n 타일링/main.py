def solution(n):
    if n < 3:
        return n
    answer = 0
    prev = [1, 2]
    for i in range(2, n):        
        answer = sum(prev) % 1000000007
        prev[0], prev[1] = prev[1], answer
    return answer % 1000000007
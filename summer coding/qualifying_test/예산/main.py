def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    d.sort()
    answer = 0
    for money in d:
        if money <= budget:
            answer += 1
            budget -= money
        else:
            break
    return answer
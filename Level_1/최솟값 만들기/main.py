def solution(A,B):
    answer = 0
    A_sorted = sorted(A)
    B_sorted = sorted(B, reverse = True)
    for i in range(len(A)):
        answer += A_sorted[i] * B_sorted[i]
    return answer
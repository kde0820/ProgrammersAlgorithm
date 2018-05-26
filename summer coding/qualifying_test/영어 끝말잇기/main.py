#-*- coding:utf-8 -*-
def solution(n, words):
    answer = []
    people = [n]
    for i in range(1, n):
        people.append(i)
    check = True
    for i in range(1, len(words)):
        if (words[i-1][-1] != words[i][0]):
            answer.append(people[(i+1)%n])
            answer.append(i//n+1)
            check = False
            break
        if words[i] in words[:i]:
            answer.append(people[(i+1)%n])
            answer.append(i//n+1)
            check = False
            break
    if check:
        answer = [0, 0]
    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
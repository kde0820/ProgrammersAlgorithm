def solution(participant, completion):
    s1 = set(participant)
    s2 = set(completion)
    if len(s1) != len(s2):
        return list(s1 - s2)[0]
    
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]
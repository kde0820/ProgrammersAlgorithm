def solution(arr):
    answer = True
    mylist = [0]*(len(arr) + 1)
    
    for i in arr:
        if i > len(arr):
            answer = False
            return answer
        if mylist[i] > 0:
            answer = False
            return answer
        mylist[i] = mylist[i] + 1
        
    if sum(mylist) == len(arr):
        answer = True
    else:
        answer = False
    return answer
def solution(arr1, arr2):
    answer = []
    if len(arr1[0]) == len(arr2):
        for row in range(len(arr1)):
            sub = []
            for i in range(len(arr2[0])):
                sum = 0
                for j in range(len(arr2)):
                    sum = sum + arr1[row][j] * arr2[j][i]
                sub.append(sum)
            answer.append(sub)   
    return answer
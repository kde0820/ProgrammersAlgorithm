def solution(s):
    answer = 1
    Matrix = [[0]*len(s) for i in range(len(s))]
    
    for i in range(len(s)):
        Matrix[0][i] = 1
        if (i+1 < len(s)) and (s[i] == s[i+1]):
            Matrix[1][i] = 2
            answer = 2

    # 홀수          
    for i in range(0, len(s) - 2, 2):
        for j in range(len(s)):
            count = Matrix[i][j]
            if count > 0:
                if(j-(i/2) > -1) and (j+(i/2) < (len(s)-1)) and (s[j-int((count+1)/2)] == s[j+int((count+1)/2)]):
                    Matrix[i+2][j] = count + 2
                    answer = Matrix[i+2][j]
    # 짝수
    for i in range(1, len(s), 2):
        for j in range(len(s)):
            count = Matrix[i][j]
            if count > 0:
                 if(j-int(count/2) > -1) and (j+int(count/2)+1 < len(s)) and (s[j-int(count/2)] == s[j+int(count/2)+1]):
                    Matrix[i+2][j] = count + 2
                    if answer < count + 2:
                        answer = count + 2       
    return answer
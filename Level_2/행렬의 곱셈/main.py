def productMatrix(A, B):
    answer = []
    if len(A[0]) == len(B):
        for row in range(len(A)):
            sub = []
            for i in range(len(B[0])):
                sum = 0
                for j in range(len(B)):
                    sum = sum + A[row][j] * B[j][i]
                sub.append(sum)
            answer.append(sub)   
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))
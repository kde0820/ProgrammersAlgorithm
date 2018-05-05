def getMinSum(A,B):
    answer = 0
    for i in range(len(A)):
        answer += min(A) * max(B)
        A.remove(min(A))
        B.remove(max(B))
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))
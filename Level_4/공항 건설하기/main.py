def chooseCity(n,city):
    answer = 0
    city.sort()
    left, right = 0, sum([x[1] for x in city])
    
    for i in range(n):
        left += city[i][1]
        right -= city[i][1]
        if right > left:
            answer = city[i+1][0]
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,5],[2,2],[3,3]]))
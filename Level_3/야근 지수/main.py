def noOvertime(n, works):
    result = 0
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    for i in range(n):
        works[works.index(max(works))] -= 1
    for num in works:
        result += num*num
    return result

print(noOvertime(4, [4, 3, 3]))
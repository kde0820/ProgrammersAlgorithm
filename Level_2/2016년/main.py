def getDayName(a,b):
    date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    total = sum(date[:a]) + b
    return day[total%7 - 1]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5, 24))
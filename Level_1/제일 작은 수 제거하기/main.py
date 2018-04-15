import copy

def rm_small(mylist):
    # 함수를 완성하세요
    if len(mylist) <= 1:
        return []
    else:
        a = copy.deepcopy(mylist)
        mylist.sort()
        l = mylist[0]
        a.remove(l)
        return a
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
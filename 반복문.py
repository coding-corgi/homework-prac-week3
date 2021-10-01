fruits = ['사과','사과','사과','사과', '배', '감', '귤']

# #사과 세기
# count = 0
# for i in fruits:
#     if i =='사과':
#         count +=1
# print(count)

# 과일 세는 함수
def fruit_name(name):
    count =0
    for i in fruits:
        if i == name:
            count +=1
    return count
print(fruit_name('사과'))
# coding: utf-8
import random
#生成随机密码
# checkcode=''
# for i in range(5):
#     current = random.randrange(0,5)
#     # if current == i:
#     #     tmp = chr(random.randint(65,90))#chr是ascii码表,65,90是（A-Z）
#     # else:
#     #     tmp = random.randint(0,9)
#     # checkcode +=str(tmp)
#     print checkcode
# print (random.random())
# print (random.uniform(1,2))
# print (random.randint(1,9))
# print (random.randrange(1000,9999))
# print (random.choice("ddssf"))
def dealerPricecalculate(a,b):
    s = random.uniform(a, b)
    return round(s,2)

def foo():
    sum = 0
    for i in range(100):
        sum += i
    return sum

if __name__ == '__main__':
    import profile
    profile.run("foo()")
    # profile.run(dealerPricecalculate(37.8,70.2))




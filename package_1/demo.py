# coding:UTF-8
""""
    用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入生成随机验证码
"""
while 1 == 1:
    def check_code():
        import random
        checkcode = ''
        for i in range(4):
            current = random.randrange(0, 4)
            if current != i:
                temp = chr(random.randint(65, 90))
            else:
                temp = random.randint(0, 9)
            checkcode += str(temp)
        return checkcode


    code = check_code()
    print(code)
    print(code)
    print(code)
    # app = input("请输入验证码：")
    # print(app)
    # if app == code:
    #     print("输入正确")
    #     break
    # else:
    #     print("输入错误")
    #     s = input("是否重新输入？yes/no")
    # if s == "no":
    #     break
    # else:
    #     continue


#j检测word  可不可以转换为数     然后判断     绝对值大于10   原样输出    绝对值小于10  正数前面+0    负数 负号和数字键+ 0
while True:
    word = input("请输入一个值（输入'q'退出）: ")
    if word.lower() == 'q':
        print("程序已退出。")
        break
    try:
        number = float(word)

        if abs(number) > 10:
            print(number)
        else:
            if number >= 0:
                print("0" + str(number))  # 正数前面加'0'
            else:
                print("-" + "0" + str(abs(number)))  # 负数前面加'-0'
    except ValueError:
        print("输入的不是有效的数字，请重新输入。")
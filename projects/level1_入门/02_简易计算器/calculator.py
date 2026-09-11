"""
项目 02：简易计算器
难度：入门 | 用时：约 40 分钟

玩法：输入两个数字和一个运算符（+ - * /），
      程序输出计算结果。支持连续计算。

本程序覆盖的知识点：
  - 函数定义与调用（def / return）
  - 字典 dict 的简单使用
  - try / except 异常处理
  - while 循环 + 退出条件
"""


def add(a, b):
    """加法"""
    return a + b


def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法：除数为 0 时报错"""
    return a / b


def main():
    print("=" * 40)
    print("简易计算器（输入 q 随时退出）")
    print("支持的运算：+ 加法 | - 减法 | * 乘法 | / 除法")
    print("=" * 40)

    # 用一个字典把运算符和对应的函数"绑定"起来
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    while True:
        # 1. 输入第一个数
        num1 = input("请输入第一个数字：")
        if num1.lower() == "q":
            break
        # 2. 输入运算符
        op = input("请输入运算符（+ - * /）：")
        if op.lower() == "q":
            break
        # 3. 输入第二个数
        num2 = input("请输入第二个数字：")
        if num2.lower() == "q":
            break

        try:
            # 把输入的字符串转成浮点数（支持小数）
            num1 = float(num1)
            num2 = float(num2)

            # 4. 从字典里取出对应的函数并调用
            if op not in operations:
                print("❌ 运算符不支持，请输入 + - * / 之一")
                continue
            result = operations[op](num1, num2)
            print(f"{num1} {op} {num2} = {result}")

        # 5. 捕获两种常见错误：
        #    - 输入了非数字
        #    - 除数为 0
        except ValueError:
            print("❌ 输入的不是有效数字，请重试")
        except ZeroDivisionError:
            print("❌ 除数不能为 0，请重试")

    print("计算器已退出，再见！")


# 只有直接运行本文件时才执行 main()
# （以后被其他文件 import 时不会自动运行）
if __name__ == "__main__":
    main()

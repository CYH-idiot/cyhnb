"""
项目 03：温度转换器
难度：入门 | 用时：约 25 分钟

玩法：输入一个摄氏温度，自动换算成华氏温度、开尔文温度。
      支持反向换算（华氏 → 摄氏）。

本程序覆盖的知识点：
  - 函数封装（把换算公式写成函数）
  - f-string 格式化输出
  - while + break 控制循环
  - 简单的输入校验

换算公式：
  华氏度 F = 摄氏度 C × 9 / 5 + 32
  开尔文 K = 摄氏度 C + 273.15
"""


def celsius_to_fahrenheit(c):
    """摄氏 → 华氏"""
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    """摄氏 → 开尔文"""
    return c + 273.15


def fahrenheit_to_celsius(f):
    """华氏 → 摄氏"""
    return (f - 32) * 5 / 9


def main():
    print("=" * 46)
    print("温度转换器")
    print("1. 摄氏 → 华氏 / 开尔文")
    print("2. 华氏 → 摄氏")
    print("输入 q 退出")
    print("=" * 46)

    while True:
        choice = input("请选择功能（1 或 2）：").strip()
        if choice.lower() == "q":
            break

        if choice == "1":
            value = input("请输入摄氏温度：")
            try:
                c = float(value)
                f = celsius_to_fahrenheit(c)
                k = celsius_to_kelvin(c)
                # :.2f 表示保留两位小数
                print(f"{c}°C = {f:.2f}°F = {k:.2f}K")
            except ValueError:
                print("❌ 请输入有效数字")
        elif choice == "2":
            value = input("请输入华氏温度：")
            try:
                f = float(value)
                c = fahrenheit_to_celsius(f)
                print(f"{f}°F = {c:.2f}°C")
            except ValueError:
                print("❌ 请输入有效数字")
        else:
            print("❌ 请输入 1 或 2")

    print("再见！")


if __name__ == "__main__":
    main()

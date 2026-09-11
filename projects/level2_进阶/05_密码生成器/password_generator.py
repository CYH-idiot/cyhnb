"""
项目 05：密码生成器
难度：进阶 | 用时：约 30 分钟

玩法：指定密码长度和包含的字符类型，生成一个强密码。

本程序覆盖的知识点：
  - random.choice() / random.shuffle()
  - 字符串操作与字符集拼接
  - 列表推导式（进阶特性）
  - 函数参数与返回值
"""

import random
import string

# 各种字符集
LOWERCASE = string.ascii_lowercase          # 小写字母 a-z
UPPERCASE = string.ascii_uppercase          # 大写字母 A-Z
DIGITS = string.digits                      # 数字 0-9
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"      # 常用符号


def generate_password(length, use_upper, use_digits, use_symbols):
    """
    根据要求生成密码。
    参数：
      length     密码长度
      use_upper  是否包含大写字母
      use_digits 是否包含数字
      use_symbols 是否包含符号
    返回：生成的密码字符串
    """
    # 1. 小写字母是"保底"字符集（永远至少包含小写字母）
    char_pool = LOWERCASE
    required = [random.choice(LOWERCASE)]  # 保证至少有一个小写

    # 2. 按需往"字符池"里加入其他字符集
    if use_upper:
        char_pool += UPPERCASE
        required.append(random.choice(UPPERCASE))
    if use_digits:
        char_pool += DIGITS
        required.append(random.choice(DIGITS))
    if use_symbols:
        char_pool += SYMBOLS
        required.append(random.choice(SYMBOLS))

    # 3. 如果长度太短，自动调整为至少能放下各类字符
    if length < len(required):
        length = len(required)

    # 4. 剩余长度从字符池里随机补足
    rest = [random.choice(char_pool) for _ in range(length - len(required))]

    # 5. 合并并打乱顺序（避免"必选字符"总在开头）
    password_chars = required + rest
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 46)
    print("密码生成器")
    print("=" * 46)

    # 1. 密码长度
    while True:
        try:
            length = int(input("请输入密码长度（建议 8~16）："))
            if length <= 0:
                print("❌ 长度必须大于 0")
                continue
            break
        except ValueError:
            print("❌ 请输入整数")

    # 2. 字符类型选择（y/n 回答）
    use_upper = input("包含大写字母？(y/n)：").strip().lower() == "y"
    use_digits = input("包含数字？(y/n)：").strip().lower() == "y"
    use_symbols = input("包含符号？(y/n)：").strip().lower() == "y"

    # 3. 生成并输出
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("\n" + "=" * 46)
    print(f"🔑 生成的密码：{password}")
    print(f"   密码长度：{len(password)}")
    print("=" * 46)


if __name__ == "__main__":
    main()

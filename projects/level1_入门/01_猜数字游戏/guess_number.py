"""
项目 01：猜数字游戏
难度：入门 | 用时：约 30 分钟

玩法：电脑随机生成一个 1~100 的整数，你不断猜，
      电脑会提示"大了/小了"，直到猜中为止。

本程序覆盖的知识点：
  - import 导入模块
  - input() 接收用户输入
  - int() 类型转换
  - if / elif / else 条件判断
  - while 循环
  - random.randint() 随机数
"""

import random

# 1. 电脑随机生成 1~100 之间的一个整数
target = random.randint(1, 100)

# 2. 记录猜了多少次
guess_count = 0

print("=" * 40)
print("欢迎来到猜数字游戏！")
print("我已经想好了一个 1~100 之间的数字")
print("=" * 40)

# 3. 进入游戏循环：只要没猜中就一直玩
while True:
    # 4. 让用户输入一个数字（input 返回的是字符串）
    guess = input("请输入你猜的数字：")

    # 5. 防止用户输入的不是数字（比如输入了"abc"）
    if not guess.isdigit():
        print("请输入一个数字哦！")
        continue  # continue = 跳过本次循环，重新开始

    # 6. 把字符串转换成整数，并累加猜的次数
    guess = int(guess)
    guess_count += 1

    # 7. 比较大小，给出提示
    if guess < target:
        print(f"小了！再大一点（你已猜 {guess_count} 次）")
    elif guess > target:
        print(f"大了！再小一点（你已猜 {guess_count} 次）")
    else:
        print("=" * 40)
        print(f"🎉 恭喜猜中！答案就是 {target}")
        print(f"你一共猜了 {guess_count} 次")
        print("=" * 40)
        break  # break = 退出循环，游戏结束

# 8. 程序结束
print("游戏结束，感谢游玩！")

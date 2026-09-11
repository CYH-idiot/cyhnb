"""
项目 04：石头剪刀布
难度：进阶 | 用时：约 45 分钟

玩法：你和电脑各出一招（石头/剪刀/布），比大小，三局两胜。

本程序覆盖的知识点：
  - random.choice() 随机选择
  - 列表 list
  - 字典 dict 的键值查找
  - 多层 if / elif 逻辑
  - 计分循环

胜负规则：
  石头 > 剪刀 > 布 > 石头
"""

import random

# 玩家可选的手势
CHOICES = ["石头", "剪刀", "布"]

# 判断胜负：玩家手势 -> 能赢电脑的什么手势
# 玩家出"石头"能赢电脑出"剪刀"……
WIN_RULES = {
    "石头": "剪刀",
    "剪刀": "布",
    "布": "石头",
}


def play_round(player_choice, computer_choice):
    """判断单局胜负，返回：玩家赢 / 电脑赢 / 平局"""
    if player_choice == computer_choice:
        return "平局"
    elif WIN_RULES[player_choice] == computer_choice:
        return "玩家赢"
    else:
        return "电脑赢"


def main():
    print("=" * 40)
    print("石头剪刀布 · 三局两胜")
    print("=" * 40)

    player_score = 0   # 玩家赢的局数
    computer_score = 0  # 电脑赢的局数

    while player_score < 2 and computer_score < 2:
        # 1. 玩家出手
        print(f"\n当前比分：你 {player_score} : {computer_score} 电脑")
        player_choice = input("请出手（石头/剪刀/布，输入 q 退出）：").strip()
        if player_choice.lower() == "q":
            break

        # 2. 检查输入是否合法
        if player_choice not in CHOICES:
            print("❌ 只能输入：石头 / 剪刀 / 布")
            continue

        # 3. 电脑随机出手
        computer_choice = random.choice(CHOICES)
        print(f"电脑出了：{computer_choice}")

        # 4. 判定本局结果
        result = play_round(player_choice, computer_choice)
        if result == "玩家赢":
            player_score += 1
            print("✅ 这局你赢了！")
        elif result == "电脑赢":
            computer_score += 1
            print("❌ 这局电脑赢了！")
        else:
            print("🤝 平局，重新来！")

    # 5. 结算
    print("\n" + "=" * 40)
    if player_score > computer_score:
        print("🎉 恭喜，你赢得了比赛！")
    elif computer_score > player_score:
        print("😅 电脑赢了，再来一局？")
    else:
        print("游戏提前结束")
    print(f"最终比分：你 {player_score} : {computer_score} 电脑")
    print("=" * 40)


if __name__ == "__main__":
    main()

"""
项目 07：猜单词游戏（Hangman）
难度：综合 | 用时：约 1 小时

玩法：电脑从词库里选一个单词，你每次猜一个字母，
      猜错一定次数（默认 6 次）就失败。

本程序覆盖的知识点：
  - 从文件读取单词库（文件 I/O）
  - 集合 set 的运用（去重、判断包含）
  - 字符串拼接生成"遮罩"
  - 随机抽取 random.choice()

运行前请确保 words.txt 与本题在同一目录。
"""

import random
import os


def load_words(file_name="words.txt"):
    """
    从单词文件读取单词列表。
    每行一个单词，去掉空白行。
    如果文件不存在，返回内置的备用词库。
    """
    builtin_words = [
        "python", "github", "computer", "programming",
        "developer", "keyboard", "network", "science",
        "internet", "software", "algorithm", "database",
    ]

    # 检查文件是否存在（os.path 是跨平台的）
    if not os.path.exists(file_name):
        print("⚠️  未找到 words.txt，使用内置词库")
        return builtin_words

    try:
        # with 语句负责自动关闭文件
        with open(file_name, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words if words else builtin_words
    except OSError:
        print("⚠️  读取文件失败，使用内置词库")
        return builtin_words


def display_progress(word, guessed_letters):
    """
    生成当前进度显示，如：p y t h _ _
    已猜对的字母显示出来，未猜对的用下划线。
    """
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def main():
    # 1. 读取词库并随机选词
    words = load_words()
    secret_word = random.choice(words)
    print(f"🤫 悄悄告诉你：单词有 {len(secret_word)} 个字母")

    guessed_letters = set()   # 所有猜过的字母（set 自动去重）
    wrong_count = 0           # 猜错次数
    max_wrong = 6             # 最多允许猜错 6 次

    while wrong_count < max_wrong:
        print("\n" + "-" * 40)
        print(f"当前进度：{display_progress(secret_word, guessed_letters)}")
        print(f"猜错的字母：{' '.join(sorted(guessed_letters)) if guessed_letters else '无'}")
        print(f"剩余机会：{max_wrong - wrong_count}")

        # 2. 玩家输入一个字母
        guess = input("请输入一个字母：").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❌ 只能输入 1 个英文字母")
            continue

        # 3. 已经猜过的字母不重复扣机会
        if guess in guessed_letters:
            print("⚠️  这个字母已经猜过了")
            continue
        guessed_letters.add(guess)

        # 4. 判断猜对还是猜错
        if guess in secret_word:
            print("✅ 猜对了！")
            # 如果所有字母都猜出来了 → 胜利
            if all(letter in guessed_letters for letter in secret_word):
                print("\n" + "=" * 40)
                print(f"🎉 恭喜！你猜出了单词：{secret_word}")
                print("=" * 40)
                return
        else:
            wrong_count += 1
            print(f"❌ 猜错了（第 {wrong_count}/{max_wrong} 次）")

    # 5. 机会用完 → 失败
    print("\n" + "=" * 40)
    print(f"😵 机会用完了！正确答案是：{secret_word}")
    print("=" * 40)


if __name__ == "__main__":
    main()

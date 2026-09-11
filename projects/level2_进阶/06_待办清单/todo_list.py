"""
项目 06：待办清单
难度：进阶 | 用时：约 50 分钟

玩法：命令行菜单管理你的待办事项：添加、查看、完成、删除。

本程序覆盖的知识点：
  - 列表 list 的增删改查
  - 字典 dict 表示一条任务
  - 死循环 + 菜单模式（经典 CLI 程序结构）
  - enumerate() 遍历带序号
"""

# 任务列表：每个任务是一个字典
# {"text": 任务内容, "done": 是否完成}
tasks = []


def show_menu():
    """打印菜单"""
    print("\n" + "=" * 40)
    print("待办清单")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 标记完成")
    print("4. 删除任务")
    print("5. 退出")
    print("=" * 40)


def add_task():
    """添加一条新任务"""
    text = input("请输入任务内容：").strip()
    if not text:
        print("❌ 任务内容不能为空")
        return
    tasks.append({"text": text, "done": False})
    print(f"✅ 已添加任务：{text}")


def show_tasks():
    """打印所有任务（带完成状态）"""
    if not tasks:
        print("📭 清单还是空的，先添加一个任务吧！")
        return
    print("\n当前任务：")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"  {index}. {status} {task['text']}")


def mark_done():
    """按序号把任务标记为完成"""
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("请输入要标记完成的任务序号："))
        task = tasks[num - 1]  # 序号从 1 开始，列表下标从 0 开始
        task["done"] = True
        print(f"✅ 已完成：{task['text']}")
    except (ValueError, IndexError):
        print("❌ 序号无效")


def delete_task():
    """按序号删除任务"""
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("请输入要删除的任务序号："))
        removed = tasks.pop(num - 1)
        print(f"🗑️  已删除：{removed['text']}")
    except (ValueError, IndexError):
        print("❌ 序号无效")


def main():
    while True:
        show_menu()
        choice = input("请选择功能（1~5）：").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("再见！")
            break
        else:
            print("❌ 请输入 1~5 之间的数字")


if __name__ == "__main__":
    main()

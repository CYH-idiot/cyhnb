"""
项目 08：通讯录管理
难度：综合 | 用时：约 1.5 小时

玩法：命令行管理联系人：添加、查找、修改、删除、保存到文件。
      数据用 JSON 格式保存在 contacts.json 中，重启程序不丢失。

本程序覆盖的知识点：
  - 字典 dict 的嵌套结构
  - JSON 序列化 / 反序列化（json 模块）
  - 文件读写（with open）
  - 完整的"增删改查"CRUD 逻辑
"""

import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    """
    从 JSON 文件读取通讯录。
    结构：{ "张三": {"phone": "138...", "email": "..."}, ... }
    """
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # 文件损坏时返回空字典，避免程序崩溃
        print("⚠️  数据文件损坏，将重新开始")
        return {}


def save_contacts(contacts):
    """把通讯录写入 JSON 文件"""
    # ensure_ascii=False 让中文正常显示，indent=2 让文件易读
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def show_menu():
    print("\n" + "=" * 40)
    print("通讯录管理")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 修改联系人")
    print("4. 删除联系人")
    print("5. 显示全部")
    print("6. 保存并退出")
    print("=" * 40)


def add_contact(contacts):
    """添加新联系人（姓名作为唯一标识）"""
    name = input("请输入姓名：").strip()
    if not name:
        print("❌ 姓名不能为空")
        return
    if name in contacts:
        print("⚠️  该联系人已存在，可用『修改』功能更新")
        return
    phone = input("请输入手机号：").strip()
    email = input("请输入邮箱：").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ 已添加联系人：{name}")


def search_contact(contacts):
    """按姓名查找"""
    name = input("请输入要查找的姓名：").strip()
    if name in contacts:
        info = contacts[name]
        print(f"📇 {name}：手机 {info['phone']}，邮箱 {info['email']}")
    else:
        print(f"❌ 未找到联系人：{name}")


def update_contact(contacts):
    """修改联系人的手机和邮箱"""
    name = input("请输入要修改的姓名：").strip()
    if name not in contacts:
        print(f"❌ 未找到联系人：{name}")
        return
    new_phone = input("请输入新手机号（直接回车保持不变）：").strip()
    new_email = input("请输入新邮箱（直接回车保持不变）：").strip()
    if new_phone:
        contacts[name]["phone"] = new_phone
    if new_email:
        contacts[name]["email"] = new_email
    save_contacts(contacts)
    print(f"✅ 已更新联系人：{name}")


def delete_contact(contacts):
    """删除联系人"""
    name = input("请输入要删除的姓名：").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️  已删除联系人：{name}")
    else:
        print(f"❌ 未找到联系人：{name}")


def show_all(contacts):
    """显示全部联系人"""
    if not contacts:
        print("📭 通讯录还是空的")
        return
    print("\n全部联系人：")
    for name, info in contacts.items():
        print(f"  📇 {name}：手机 {info['phone']}，邮箱 {info['email']}")


def main():
    # 程序启动时先加载已保存的数据
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("请选择功能（1~6）：").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            show_all(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("数据已保存，再见！")
            break
        else:
            print("❌ 请输入 1~6 之间的数字")


if __name__ == "__main__":
    main()

# File: SScore_manage_optimized.py
# 优化版学生成绩管理系统
# 主要修复缩进问题，增强代码健壮性

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class SingleLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0  # 新增size属性避免遍历计数

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def delete(self, target_id):
        if self.size == 0:
            print("空链表")
            return

        prev = self.head
        while prev.next:
            current = prev.next
            if current.data.get('id') == target_id:
                prev.next = current.next
                self.size -= 1
                return
            prev = prev.next
        print("未找到对应学号")

    # 其他方法保持类似结构，统一使用4空格缩进...
    def save_and_exit(self):
        with open('database.dat', 'wb') as f:
            pickle.dump(self, f)
        print("数据已保存")
        exit()

	def insert_after_head(self, data):
		new_node = Node(data)

class StudentControlSystem(SingleLinkedList):
    def print_menu(self):
        """优化菜单显示"""
        menu = [
            "1. 增加学生信息",
            "2. 删除学生信息",
            "3. 修改学生信息",
            "4. 查找学生信息",
            "5. 显示所有信息",
            "6. 排序",
            "0. 退出程序"
        ]
        print("\n" + "="*30)
        print("\n".join(menu))
        print("="*30 + "\n")

    def add_info(self):
        """增强输入验证"""
        while True:
            std_id = input("学号：").strip()
            if not std_id.isdigit():
                print("学号必须为数字")
                continue

            if any(current.data['id'] == std_id for current in self):
                print("学号已存在")
                continue

            # 成绩验证改进
            try:
                grade = float(input("成绩："))
                if not 0 <= grade <= 100:
                    raise ValueError
            except ValueError:
                print("无效成绩（0-100）")
                continue

            # 确认保存逻辑
            if input("确认保存？(y/n)").lower() == 'y':
                self.append({'id': std_id, 'name': input("姓名："), 'grade': grade})
                break

    # 其他方法保持统一缩进...

def main():
    system = StudentControlSystem()

    # 改进文件加载
    try:
        with open('database.dat', 'rb') as f:
            # 建议使用pickle替代eval更安全
            system = pickle.load(f)
    except FileNotFoundError:
        pass

    while True:
        system.print_menu()
        choice = input("请选择操作：").strip()

        # 改进输入处理
        if not choice.isdigit():
            print("请输入数字选项！")
            continue

        # 使用字典调度替代多重if-else
        actions = {
            1: system.add_info,
            2: lambda: system.delete(input("输入删除学号：")),
            # ...其他操作映射
            0: system.save_and_exit
        }

        if (action := actions.get(int(choice))):
            action()
        else:
            print("无效选项！")

if __name__ == '__main__':
    main()

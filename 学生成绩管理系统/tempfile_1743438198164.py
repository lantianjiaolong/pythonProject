# 学生成绩管理系统优化版
# 修复缩进问题，增强健壮性，优化代码结构

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class SingleLinkedList:
    def __init__(self):
        self.head = Node()
        self.pointer = self.head
        self.size = 0  # 新增size属性优化计数

    def append(self, data):
        new_node = Node(data)
        self.pointer.next = new_node
        self.pointer = new_node
        self.size += 1

    def delete(self, target):
        if self.size == 0:
            print("链表为空")
            return False
        
        current = self.head
        while current.next:
            if current.next.data == target:
                deleted_node = current.next
                current.next = deleted_node.next
                if deleted_node == self.pointer:  # 处理删除尾节点情况
                    self.pointer = current
                self.size -= 1
                del deleted_node
                return True
            current = current.next
        print("未找到目标数据")
        return False

    def insert_after_head(self, data):
        new_node = Node(data)
        if not self.head.next:
            self.head.next = new_node
            self.pointer = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        self.size += 1

    def reverse(self):
        reversed_list = SingleLinkedList()
        current = self.head.next
        while current:
            reversed_list.insert_after_head(current.data)
            current = current.next
        return reversed_list

    def sort(self):
        if self.size < 2:
            return
        
        for i in range(self.size-1):
            current = self.head.next
            swapped = False
            for j in range(self.size-1-i):
                if current.data > current.next.data:
                    # 交换节点数据
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
            if not swapped:
                break

    def display(self):
        current = self.head.next
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

class StudentControlSystem(SingleLinkedList):
    MENU_ITEMS = [
        "1. 添加学生信息",
        "2. 删除学生信息",
        "3. 修改学生信息",
        "4. 查找学生信息",
        "5. 显示所有信息",
        "6. 排序信息",
        "0. 退出系统"
    ]

    def __init__(self):
        super().__init__()
        self.load_data()

    def print_menu(self):
        print("\n" + "="*30)
        print("{:^28}".format("学生成绩管理系统"))
        print("-"*30)
        for item in self.MENU_ITEMS:
            print(f"| {item:<26} |")
        print("="*30)

    def load_data(self):
        try:
            with open('students.dat', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data = eval(line.strip())
                        self.append(data)
            print("数据加载成功！")
        except (FileNotFoundError, SyntaxError):
            print("未找到数据文件或数据损坏，已创建新数据库")

    def save_data(self):
        with open('students.dat', 'w', encoding='utf-8') as f:
            current = self.head.next
            while current:
                f.write(f"{current.data}\n")
                current = current.next

    def is_id_unique(self, std_id):
        current = self.head.next
        while current:
            if current.data["id"] == std_id:
                return False
            current = current.next
        return True

    def add_student(self):
        while True:
            try:
                std_id = input("请输入学号：").strip()
                if not std_id.isdigit():
                    raise ValueError("学号必须为数字")
                
                if not self.is_id_unique(std_id):
                    print("该学号已存在！")
                    continue

                name = input("请输入姓名：").strip()
                if not name:
                    raise ValueError("姓名不能为空")

                grade = float(input("请输入成绩（0-100）："))
                if not 0 <= grade <= 100:
                    raise ValueError("成绩超出范围")

                confirm = input(f"确认添加 {name}（学号：{std_id} 成绩：{grade}）吗？(y/n)").lower()
                if confirm in ('y', 'yes'):
                    self.append({
                        "id": std_id,
                        "name": name,
                        "grade": grade
                    })
                    print("添加成功！")
                    break
                else:
                    print("已取消添加")
                    break

            except ValueError as e:
                print(f"输入错误：{e}")

    def delete_student(self):
        std_id = input("请输入要删除的学号：").strip()
        current = self.head.next
        while current:
            if current.data["id"] == std_id:
                confirm = input(f"确认删除 {current.data['name']} 吗？(y/n)").lower()
                if confirm in ('y', 'yes'):
                    self.delete(current.data)
                    print("删除成功！")
                    return
                else:
                    print("已取消删除")
                    return
            current = current.next
        print("未找到该学号对应的学生")

    def modify_student(self):
        std_id = input("请输入要修改的学号：").strip()
        current = self.head.next
        while current:
            if current.data["id"] == std_id:
                print("当前信息：")
                print(f"姓名：{current.data['name']}")
                print(f"成绩：{current.data['grade']}")
                
                try:
                    new_name = input("新姓名（留空保持原值）：").strip()
                    new_grade = input("新成绩（留空保持原值）：").strip()
                    
                    if new_name:
                        current.data["name"] = new_name
                    if new_grade:
                        grade = float(new_grade)
                        if 0 <= grade <= 100:
                            current.data["grade"] = grade
                        else:
                            print("成绩范围无效，保持原值")
                    
                    print("修改成功！")
                    return
                except ValueError:
                    print("无效的成绩输入")
                    return
            current = current.next
        print("未找到该学号对应的学生")

    def search_student(self):
        std_id = input("请输入要查找的学号：").strip()
        current = self.head.next
        while current:
            if current.data["id"] == std_id:
                print("\n查询结果：")
                print(f"学号：{current.data['id']}")
                print(f"姓名：{current.data['name']}")
                print(f"成绩：{current.data['grade']}")
                return
            current = current.next
        print("未找到该学号对应的学生")

    def display_all(self):
        if self.size == 0:
            print("暂无学生信息")
            return
        
        print("\n{:<10} {:<10} {:<10}".format("学号", "姓名", "成绩"))
        print("-"*30)
        current = self.head.next
        while current:
            data = current.data
            print("{:<12} {:<10} {:<8}".format(
                data["id"], 
                data["name"], 
                data["grade"]
            ))
            current = current.next

    def sort_students(self):
        if self.size == 0:
            print("没有可排序的数据")
            return
        
        print("\n排序选项：")
        print("1. 按学号排序")
        print("2. 按成绩排序")
        choice = input("请选择排序方式：").strip()
        
        reverse_flag = False
        order_choice = input("排序顺序（1.升序 2.降序）：").strip()
        if order_choice == "2":
            reverse_flag = True

        current = self.head.next
        students = []
        while current:  # 转换为列表排序更高效
            students.append(current.data)
            current = current.next

        try:
            if choice == "1":
                students.sort(key=lambda x: int(x["id"]), reverse=reverse_flag)
            elif choice == "2":
                students.sort(key=lambda x: float(x["grade"]), reverse=reverse_flag)
            else:
                print("无效选项")
                return
        except ValueError:
            print("数据格式错误，排序失败")
            return

        # 重建链表
        self.head = Node()
        self.pointer = self.head
        self.size = 0
        for student in students:
            self.append(student)
        
        print("排序完成！")

    def run(self):
        while True:
            self.print_menu()
            choice = input("请输入操作编号：").strip()
            
            actions = {
                "1": self.add_student,
                "2": self.delete_student,
                "3": self.modify_student,
                "4": self.search_student,
                "5": self.display_all,
                "6": self.sort_students,
                "0": lambda: (self.save_data(), exit())
            }
            
            if choice in actions:
                actions[choice]()
            else:
                print("无效的输入，请重新选择")

if __name__ == "__main__":
    system = StudentControlSystem()
    try:
        system.run()
    except KeyboardInterrupt:
        system.save_data()
        print("\n数据已保存，程序退出")

import json

from Student import Student
# 创建学生（json字符串形式）
def create_student():
    # 读取旧学生列表
    student_list = read_student_list_from_json()
    # 把从键盘接受的数据封装成字典
    new_student = get_student_data()
    # 判断是否已经存在
    for s in student_list:
        if s["id"] == new_student.sid:
            print(f"{new_student.sid}已存在，请重新输入")
            get_student_data()
    # 格式化新学生为json
    new_student_json = json.dumps(new_student,ensure_ascii=False,indent=2)
    # 将新学生插入旧列表
    student_list.append(new_student_json)
    # 写文件
    with open("./students.json","w",encoding="utf-8") as f:
        json.dump(student_list,f,ensure_ascii=False,indent=2)
    return "添加成功"
def read_student_list_from_json():
    with open("./students.json","r") as f:
        student_json = json.loads(f.read())
        student_list = list(student_json)
        return student_list

def get_student_data():
    s_id = int(input("Enter student ID: "))
    s_name = int(input("Enter student name: "))
    s_age = int(input("Enter student age: "))
    s_gender = int(input("Enter student gender: "))
    s_grades = int(input("Enter student grades: "))
    new_student = Student(s_id, s_name, s_age, s_gender, s_grades)
    return new_student

import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Student.from_dict(d) for d in data]
    except (json.JSONDecodeError, KeyError) as e:
        print(f"数据文件损坏，无法读取：{e}")
        return []


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students],
                  f, ensure_ascii=False, indent=2)


def input_score(subject):
    while True:
        raw = input(f"请输入 {subject} 成绩（0~100）：").strip()

        if not raw.isdigit():
            print("请输入数字")
            continue

        score = int(raw)
        if not 0 <= score <= 100:
            print("成绩必须在 0~100 之间")
            continue

        return score


def add_student(students):
    name = input("请输入学生姓名：").strip()

    if not name:
        print("姓名不能为空")
        return

    if any(s.name == name for s in students):
        print(f"{name} 已存在")
        return

    chinese = input_score("语文")
    math = input_score("数学")
    english = input_score("英语")

    students.append(Student(name, chinese, math, english))
    save_students(students)
    print(f"已添加：{name}")

HEADER = f"{'姓名':<8}{'语文':>6}{'数学':>6}{'英语':>6}{'总分':>8}{'平均':>8}"
LINE = "-" * 42


def show_all(students):
    if not students:
        print("暂无数据")
        return

    print(HEADER)
    print(LINE)
    for s in students:
        print(s)


def find_student(students):
    name = input("请输入要查找的姓名：").strip()
    result = [s for s in students if s.name == name]

    if not result:
        print("未找到")
    else:
        print(HEADER)
        for s in result:
            print(s)


def delete_student(students):
    name = input("请输入要删除的姓名：").strip()
    before = len(students)

    students[:] = [s for s in students if s.name != name]

    if len(students) == before:
        print("未找到该学生")
    else:
        save_students(students)
        print(f"已删除：{name}")

import csv


def show_stats(students):
    if not students:
        print("暂无数据")
        return

    avg_scores = [s.average() for s in students]
    total_scores = [s.total() for s in students]
    pass_count = sum(1 for a in avg_scores if a >= 60)

    print(f"学生人数：{len(students)}")
    print(f"平均分：{sum(avg_scores) / len(avg_scores):.2f}")
    print(f"最高总分：{max(total_scores)}")
    print(f"最低总分：{min(total_scores)}")
    print(f"及格人数：{pass_count}")
    print(f"及格率：{pass_count / len(students) * 100:.1f}%")


def sort_students(students):
    sorted_list = sorted(students, key=lambda s: s.total(), reverse=True)
    show_all(sorted_list)


def export_csv(students):
    if not students:
        print("暂无数据")
        return

    filename = "students_export.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["姓名", "语文", "数学", "英语", "总分", "平均分"])
        for s in students:
            writer.writerow([
                s.name, s.chinese, s.math, s.english,
                s.total(), round(s.average(), 1),
            ])
    print(f"已导出：{filename}")

def menu():
    print()
    print("===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查看全部")
    print("3. 查找学生")
    print("4. 删除学生")
    print("5. 查看统计")
    print("6. 按总分排序")
    print("7. 导出 CSV")
    print("0. 退出")


def main():
    students = load_students()
    print(f"已加载 {len(students)} 条记录")

    while True:
        menu()
        choice = input("请选择：").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            show_stats(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            export_csv(students)
        elif choice == "0":
            print("再见")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    main()
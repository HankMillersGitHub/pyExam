# 用列表存五个成绩 求平均分最高分
# score = [46,65,68,94,32]
# score.sort()
# print(f"最高分是：{score[len(score) - 1]}")
# sum = 0
# for num in score:
#     sum += num
# print(f"平均分是：{sum // len(score)}")

score = [46,65,68,94,32]
print(f"最高分是：{max(score)}")
print(f"平均分是：{sum(score) // len(score)}")

# 用字典存三个学生的姓名和分数，打印分数最高的学生  (ps:感觉我这个题写复杂了 应该有更好的办法)
# students = {"student1":{"name":"张三","score":90},
#             "student2":{"name": "李四","score": 80},
#             "student3":{"name": "王五","score": 70}}
# maxScore = 0
# maxKey = ""
# for k,v in students.items():
#     if v["score"] > maxScore:
#         maxScore = v["score"]
#         maxKey = k
# print(f"the max score is belong to: {maxKey}")

students = {"张三":80,"李四":90,"王五":100}
top = max(students,key=students.get)
print(f"最高分是{students[top]},学生是{top}")
# 用集合找出两个列表的重复元素
# list1 = [1,2,3]
# list2 = [1,2,3,4,5,6]
# set1 = set(list1)
# set2 = set(list2)
# print(set1 - (set1 - set2))
list1 = [1,2,3]
list2 = [1,2,3,4,5,6]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
students = ["张三","李四","王五","赵六"]
# 把学生列表存储为json 并且读出来再次打印
# import json
# s = json.dumps(students.json,ensure_ascii=False,indent=2)
# with open("./exam_docs/_03_json.json","w",encoding="utf-8") as f:
#     f.write(s)
#
# with open("./exam_docs/_03_json.json","r",encoding="utf-8") as f:
#     print(f.read())


# 同样的数据存储为csv
import csv
with open("./exam_docs/_03_json.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name"])
    for student in students:
        writer.writerow([student])

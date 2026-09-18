# 把1-10写入文件 每行一个数字
# with open("./exam_docs/_01_file_exam.txt", "a",encoding="utf8") as f:
#     for i in range(1,10):
#         f.write(f"{str(i)}\n")
#
# 把上题中的数字读取出来并且求和
numbers = []
with open("./exam_docs/_01_file_exam.txt", "r",encoding="utf8") as f:
    for line in f:
        numbers.append(int(line.strip()))
print(sum(numbers))
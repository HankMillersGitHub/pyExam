import os
# 获取当前目录
print(os.getcwd())
# 创建目录
# os.makedirs("./_01_os_exam",exist_ok=True)
# 判断目录是否存在
print(os.path.exists("./_01_os_exam"))
# 专门用于拼接文件目录
print(os.path.join("_01_os_exam", "test.txt"))
# 列出文件和目录
print(os.listdir("./"))
# 文件重命名 文件删除
os.rename("old_name", "new_name")
os.remove("remove_name")
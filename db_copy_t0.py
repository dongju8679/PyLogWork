import shutil
import datetime
import os
from distutils.dir_util import copy_tree

src_path = r"D:\\PythonProjects\\MyKiwoom\\database\\"
file_list = os.listdir(src_path)
dst_path = r"D:\\database\\kiwoomdb\\{:%Y%m%d}\\".format(datetime.datetime.now())
if not os.path.exists(dst_path):
    os.makedirs(dst_path)
    for file in file_list:
        new_path = shutil.move(f"{src_path}/{file}", f"{dst_path}/{file}")
        print(new_path)


# src_path = r"D:\tzwork\db_study\database\\"
# # if not os.path.exists(src_path):
# #     os.makedirs(src_path)
# print("src_path = ", src_path)
# # src_path = "D:\\tzwork\\db_study\\database"
# # src_file = r"tick_.db"
# # source = r"i1.png"
# file_list = os.listdir(src_path)
# # print("file_list = ", file_list)
# dst_path = r"D:\\database\\kiwoomdb\\{:%Y%m%d}\\".format(datetime.datetime.now())
# # dst_path = "D:/database/kiwoomdb/{:%Y%m%d}".format(datetime.datetime.now())
# # if not os.path.exists(dst_path):
# #     os.makedirs(dst_path)
# # dst_file = r"tick_.db"
#
# print("before copy")
# # print(os.listdir(src_path))
#
# # copy_tree(src_path, dst_path)
# # shutil.move(src_path, dst_path)
# if not os.path.exists(dst_path):
#     os.makedirs(dst_path)
#     for file in file_list:
#         new_path = shutil.move(f"{src_path}/{file}", f"{dst_path}/{file}")
#         print(new_path)
#
# # shutil.copyfile(src_path + src_file, dst_path + dst_file)
# # shutil.copy2(path + source,path + destination)
# print("after copy")
# # print(os.listdir(dst_path))
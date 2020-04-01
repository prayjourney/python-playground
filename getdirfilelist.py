# -*- coding = utf-8 -*-
import os


def fileAndDir(root, file_list, dir_list):
    """
    获取一个文件夹的下面的所有的文件列表
    """
    list1 = os.listdir(root)
    for x in range(len(list1)):
        full_file_str = root + "//" + list1[x]
        if (os.path.isfile(full_file_str)):
            file_list.append(full_file_str)
        if (os.path.isdir(full_file_str)):
            fileAndDir(full_file_str, file_list, dir_list)


if __name__ == '__main__':
    file_list = []
    dir_list = []
    root = "C:\\Users\\Administrator\\Pictures\\iCloud Photos"
    fileAndDir(root, file_list, dir_list)
    print(file_list)
    print(len(file_list))

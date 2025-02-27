# -*- coding = utf-8 -*-
import os


def get_file_full_path(root, file_list):
    """
        获取一个path的文件全路径，path可以是文件或者文件夹
    """
    if (os.path.isfile(root)):
        file_list.append(root)
    else:
        file_dir(root, file_list)

    return file_list


def file_dir(root, file_list):
    """
        获取一个文件夹下面的所有文件的全路径
    """
    list1 = os.listdir(root)
    for x in range(len(list1)):
        full_file_str = root + "//" + list1[x]
        if (os.path.isfile(full_file_str)):
            file_list.append(full_file_str)
        if (os.path.isdir(full_file_str)):
            file_dir(full_file_str, file_list)


if __name__ == '__main__':
    file_list = []
    dir_list = []
    root = "/Users/zgy/mycode/python-projects/python-playground"
    file_dir(root, file_list)
    print(file_list)
    print(len(file_list))

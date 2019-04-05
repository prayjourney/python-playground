# -*- coding = utf-8 -*-
import os
# import time


def getPathFileList(root):
    '''
        获取一个path下面的所有符合条件的文件全路径,
        path可以是文件或者文件夹, 返回符合条件文件的全路径的列表
    '''
    file_list = []
    if(os.path.isfile(root)):
        file_list.append(root)
    else:
        getDirFileList(root, file_list)

    return file_list


def getDirFileList(root, file_list):
    '''
        获取一个文件夹下面的所有符合过滤条件的文件全路径
    '''
    list1 = os.listdir(root)
    for x in range(len(list1)):
        full_file_str = root + "//" + list1[x]
        if(os.path.isfile(full_file_str) and full_file_str.endswith(".md")):
            file_list.append(full_file_str)
        if(os.path.isdir(full_file_str)):
            getDirFileList(full_file_str, file_list)


def appendInfo4File(file_path, list_info):
    """
    作用:
        给一个文件首行添加需要的内容, 如果已有则不添加
    参数:
        filepath:是文件的路径
        list_info:是我们需要添加的信息, 可以有多个最少一个
    """
    # 使用a采用追加模式, 将光标放到第一行也可以完成操作
    with open(file_path, 'r+', encoding='utf-8') as f:
        # 获取文件名
        file_title = "title: " + os.path.split(file_path)[-1].split(".")[0] + "\n"
        list_info[1] = file_title
        # 对第一行的数据进行分析, 如果已经有了想要加入的内容,则不再去添加
        size = len(list_info)
        content_temp = f.readline()
        # 使用readline来完成读取文件内容的任务, 查看第一行的内容是否重复即可
        if(list_info[0] == content_temp):
            return
        else:
            # 将list_info之中的内容写入到文本之中
            data = f.read()
            str = ""
            for x in range(size):
                str = str + list_info[x]
            
            # 不能丢了标题
            str_content = str + content_temp + data
        # 字符指针跳到第一行, 添加指定的内容
        f.seek(0)
        f.write(str_content)


def writeInfo4FileList(path, info):
    file_list = getPathFileList(path)
    size_list = len(file_list)
    if(size_list == 0):
        raise "file_list is null! please check!"
    else:
        for file_index in range(size_list):
            appendInfo4File(file_list[file_index], info)


if __name__ == '__main__':
    str_first = "---\n"
    str_title = ""
    str_date = "date: x \n"
    str_tags = "tags:\n  - X\n  - X\n  - X\n"
    str_categories = "categories:\n  - X\n  - X\n"
    str_last = "---\n"
    info_list = [str_first, str_title, str_date, str_tags, str_categories, str_last]
    writeInfo4FileList("C://src-repo//hexo-blog//source//_posts", info_list)
    print("okay")

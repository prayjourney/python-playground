# -*- encoding: utf-8 -*-
import os, time

'''
class和method的定义和创建方法
'''


# class
class Test:
    role = 'person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(str(self.name) + "," + str(self.age))


# method
def iom(x):
    for x in range(10):
        print(123)


"""
作用:

    在以md结尾的文件之中, 在首行添加需要的内容
参数:
    filepath是文件的路径
    list_info是我们需要添加的信息，可以有多个最少一个
"""


def fileAppend(filepath, list_info):
    # 获取文件创建,修改,上次访问时间
    cTime = os.path.getctime(filepath)
    mTime = os.path.getmtime(filepath)
    aTime = os.path.getatime(filepath)
    cTimeArray = time.localtime(cTime)
    mTimeArray = time.localtime(mTime)
    aTimeArray = time.localtime(aTime)
    cStrTime = time.strftime("%Y-%m-%d %H:%M:%S", cTimeArray)
    mStrTime = time.strftime("%Y-%m-%d %H:%M:%S", mTimeArray)
    aStrTime = time.strftime("%Y-%m-%d %H:%M:%S", aTimeArray)
    print("文件创建时间:" + cStrTime)
    print("文件创建时间:" + mStrTime)
    print("文件上次访问时间:" + aStrTime)

    # 使用a采用追加模式, 将光标放到第一行也可以完成操作
    with open(filepath, 'r+', encoding='utf-8') as f:
        # 对前n行的数据进行分析, 如果已经有了想要加入的内容,则不再去添加
        # 使用readline来完成读取文件内容的任务
        size = len(list_info)
        contentTemp = f.readline()
        cur = 0
        while cur < size:
            if (contentTemp == list_info[cur]):
                return
            else:
                cur = cur + 1

        # 将list_info之中的内容写入到文本之中
        data = f.read()
        str = ""
        for x in range(size):
            str += list_info[x]
            print(data)
        str_content = str + data

        # 字符指针跳到第一行, 添加指定的内容
        f.seek(0)
        f.write(str_content)
        # pip install pylint flake8 flake8+yapf+pep8


"""
作用:
    返回给出的文件夹下面的所有的文件的列表
参数:
    filepath是文件的路径
"""


def getPathOrFileList(filePath):
    fileList = []
    if (os.path.isfile(filePath)):
        fileList.append(filePath)
    else:
        # #列出文件夹下所有的目录与文件
        for root, dirs, files in os.walk(filePath):
            for temp_file in files:
                # 使用后缀的方式进行过滤
                try:
                    if (temp_file.endswith("json")):
                        fileList.append(temp_file)
                except Exception as e:
                    print(e)
    return fileList


if __name__ == '__main__':
    str1 = "title : ada11das3\n"
    str2 = "name \n"
    str3 = "hello \n"
    list = [str1, str2, str3]
    print(list[0])
    print(len(list))
    print(getPathOrFileList("C://Users//Administrator//Desktop//111"))
    print(os.name)
    # fileAppend("C://Users//r00478401//Desktop//le//testfile.txt", list)
    # iom(10)
    # print(range(10))
    # t =test(1123,22)
    # print(t.role)
    # t.getInfo()
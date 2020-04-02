"""
操作文件，处理异常
"""

import os
import time


def do_file(path):
    # ========= ===============================================================
    # Character Meaning
    # --------- ---------------------------------------------------------------
    # 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)
    # '+'       open a disk file for updating (reading and writing)
    # 'U'       universal newline mode (deprecated)
    # ========= ===============================================================
    print(path)
    # 打开
    f = open(path, 'r', encoding='utf-8')
    f.close()

    f = open(path, 'a+t', encoding='utf-8')
    f.write("中国人民")
    f.writelines("\n小日本，小日本")
    f.close()


def write_poem(path):
    cipaiming = '临江仙·柳絮'
    zuozhechaodai = '    清 曹雪芹'
    diyiju = '白玉堂前春解舞，东风卷得均匀。蜂围蝶阵乱纷纷。'
    dierju = '几曾随逝水？岂必委芳尘？'
    disanju = '万缕千丝终不改，任他随聚随分。韶华休笑本无根。'
    disiju = '好风凭借力，送我上青云。'

    # 文件是否存在
    is_exist_file = os.path.exists(path)
    file_info = "文件已经存在"
    if is_exist_file is False:
        file_info = "文件不存在"

    # 如果存在，那么就删除掉，重新写入
    if file_info == "文件已经存在":
        os.remove(path)

    print(path + ", " + file_info + ", " + str(time.time()))
    f = open(path, mode='x+', encoding='utf-8')
    f.writelines(cipaiming + "\n")
    f.writelines(zuozhechaodai + "\n")
    f.writelines(diyiju + "\n")
    f.writelines(dierju + "\n")
    f.writelines(disanju + "\n")
    f.writelines(disiju + "\n")
    f.close()


#  异常的解决
def file_exception(path):
    try:
        if False is os.path.exists(path):
            print("路径存在，是： " + str(str))
        else:
            5 / 0
    except FileExistsError:
        print("文件未找到！！！")
    except IOError:
        print("发生了IOError")
    except ZeroDivisionError:
        print("ZeroDivisionError!!!")
    finally:
        print("hello, 异常都处理完毕了！！！")


if __name__ == '__main__':
    path = 'D:\\hello.txt'
    do_file(path)
    path2 = "D:\\临江仙·柳絮.txt"
    write_poem(path2)
    file_exception(path2)
# coding =utf8

def inputwords(path):
    """
    持续输入文字
    """
    with open(file=path, mode="a+", encoding="utf8") as f:
        x = input()
        while (x != "quit"):
            """
            持续输入, 直到输入quit, 才退出
            """
            f.write(x + "\n")
            x = input()
    print("输入完毕.")
    # python文件读写模式的总结
    # https://www.cnblogs.com/zhxwind/p/8761618.html
    # https://www.cnblogs.com/dadong616/p/6824859.html


def getinputcontent(path):
    """
    获取输入的内容
    """
    with open(file=path, mode="r+", encoding="utf8") as f:
        all_content = f.read()
        print(all_content)


if __name__ == "__main__":
    path = "zen.txt"
    print("即将开始输入工作...\n")
    inputwords(path)
    print("内容是:\n")
    getinputcontent(path)

# coding:utf-8


class InnerDataStructure:
    """
    四大内置元素，都可以通过xxx[1]， xxx[index]这种方式来获取值
    而xxx(a)，这种方式，是调用方法，然后传入参数的方式
    """

    def __init__(self):
        pass

    # 使用列表
    def useList(self):
        mylist = [1, 2, 3, 4, 5]
        print(len(mylist))
        print(mylist.pop(2))
        print(mylist[2])
        mylist.append("hello")
        print(mylist)
        mylist.remove(2)
        print(mylist)

    # 使用字符串
    def useStr(self):
        str = "张飞啊啊啊啊 第三方第三方士大夫   ss"
        print(str)
        print(len(str))
        print(str.upper())

    # 使用元组 tuple
    def useTuple(self):
        mytuple = (1, 2, 3, 4, 5, 6, 9, "helloworld", "what", 99, 2, 6, 3)
        print(mytuple[2])
        print(mytuple.count(6))
        print("mytuple的长度是: " + str(len(mytuple)))
        for x in mytuple:
            print("x： " + str(x))

    def useSet(self):
        # [1, 2, 3, 4]===>TypeError: unhashable type: 'list'
        # myset = {1, 2, 3, 4, "sdfsajk", "fffd", [1, 2, 3, 4], (1, 2, 34, "1312")}
        myset = {1, 2, 3, 4, "sdfsajk", "fffd", (1, 2, 34, "1312")}
        myset.add("111")
        # print(myset), TypeError: 'set' object is not subscriptable
        # myset[1]
        print(str(myset.pop()) + str(" ,============"))
        print(str("myset包含'fffd'元素：") + myset.__contains__("fffd").__str__())
        print("123123213")
        print("不同的部分：" + str(myset.difference({1, 2, 3, 4})))

    def useDictionary(self):
        mydic = {"name": "张三", "age": 25, "address": "成都郫县"}
        print(mydic)
        print(mydic.get("name"))
        mydic.update({"hobby": "旅游", "college": "东京帝国大学"})
        print(mydic)
        # mydic.update({"hobby": "旅游", "college": "东京帝国大学"},
        #              {"住址": "熊本县", "吉祥物": "熊本熊"},
        #              {"偶像": "特朗普"})
        mydic.pop("name")
        print(mydic.keys())

    # 类的内部使用lambda表达式
    lam = lambda self, aa: aa * aa


# 这个是文件之中的方法，不是类方法
def opt_file(file_path):
    t = open(file_path, 'r')  # 打开文件路径
    print(t.closed)
    t.close()


class Girl:
    # 类变量
    info = '88元人民币'

    # 不需要定义变量, 只能有一个初始化函数吗？
    # !!!一个类只能有一个init初始化函数!!!
    # https://zhidao.baidu.com/question/1370573407628809939.html
    # def __init__(self, name):
    #     self.name = name

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("name is " + str(self.name))

    def print_all_info(self):
        print("name is " + str(self.name) + "age is " + str(self.age))


# 使用lambda表达式，在类的外部使用
my_lambda = lambda a1, a2: a1 if a1 > a2 else a2

if __name__ == '__main__':
    ids = InnerDataStructure()
    ids.useList()
    ids.useStr()
    ids.useTuple()
    ids.useSet()
    ids.useDictionary()
    print(ids.lam(33))
    print("use lambda...")
    print(my_lambda(1, 2))
    # for 循环
    for x in "hello world":
        print(x + "   x")

    # 切片,https://www.cnblogs.com/huoxn/p/10900226.html
    list = ['zhangsan', 3307, 18, 1280, 'cc', 'lisi', 25.62, 5, '王五', 'lilei']
    print(list[1:4])  # [1,4)
    print(list[1:-1])

    opt_file("D:\\临江仙·柳絮.txt")

    girlA = Girl("张三", 23)
    # 添加新的变量
    girlA.__setattr__("location", "CD")
    girlB = Girl("小红", 22)
    girlA.print_name()
    girlB.print_all_info()
    print(girlA.info)
    print(Girl.info)

# coding:utf-8

class InnerDataStructure:
    def __init__(self):
        pass

    # 使用列表
    def useList(self):
        mylist = [1, 2, 3, 4, 5]
        print(len(mylist))
        print(mylist.pop(2))
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
        print(mytuple.count(6))
        print("mytuple的长度是: " + str(len(mytuple)))
        # for x in mytuple:
        #     print("x： " + str(x))

    def useSet(self):
        # [1, 2, 3, 4]===>TypeError: unhashable type: 'list'
        # myset = {1, 2, 3, 4, "sdfsajk", "fffd", [1, 2, 3, 4], (1, 2, 34, "1312")}
        myset = {1, 2, 3, 4, "sdfsajk", "fffd", (1, 2, 34, "1312")}
        myset.add("111")
        print(myset)
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

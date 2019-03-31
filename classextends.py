# coding = utf-8
'''
继承之中的问题:
1.继承的语法, 主要是对于构造函数的调用
先后顺序, 先调用第一个继承的类, 后续依次序调用, 子类的参数自行实例化
https://www.cnblogs.com/ExMan/p/8457121.html
2.对于父类方法的复写
直接在子类之中覆盖父类的方法, 同名写入方法体新的内容就可以了
3.对于父类方法的调用

'''


class Animal:
    '''
    动物类
    '''
    def __init__(self, kind):
        self.kind = kind

    def getkind(self):
        return self.kind


class Bear(Animal):
    '''
    熊
    '''
    # python之中只能定义一个构造函数?------>貌似只能有一个构造函数
    # 第一个继承构造函数
    def __init__(self, kind, weight, color):
        Animal.__init__(self, kind)
        self.weight = weight
        self.color = color

    # 第二个继承构造函数
    # def __init__(self, kind, color):
        # Animal.__init__(self, kind)
        # self.color = color

    def getinfo(self):
        strinfo = ""
        # hasattr判断某个对象是否有某属性
        if(hasattr(self, "kind")):
            strinfo = "kind is: " + self.kind

        if(hasattr(self, "origin")):
            strinfo = "origin is: " + self.origin

        if(hasattr(self, "origin")):
            strinfo = "color is: " + self.color

        return strinfo


class People(Animal):
    '''
    人
    '''
    # 使用super的方式来定义构造函数
    def __init__(self, kind, nation):
        # super这种调用不行了？
        # super(Animal, self).__init__(self, kind)
        Animal.__init__(self, kind)
        self.nation = nation

    def peopeinfo(self):
        return "info is :" + self.kind + ", " + self.nation

    def getkind(self):
        return ("这是一个" + self.kind + "aaa!")


class Land:
    '''
    土地
    '''
    def __init__(self, land_name):
        self.land_name = land_name

    def getlandname(self):
        return self.land_name


# class Taiwangirl(People, Land):
# def __init__(self, kind, nation, land_name, profession):
# super(People, self).__init__(self, kind, nation)
# super(Land, self).__init__(self, land_name)
# self.profession = profession

# # 改写方法
# def getlandname(self):
# landinfo = self.land_name + " , i love it!"
# rerurn landinfo

# def getprofesssion(self):
# return self.profession

# def peopeinfo(self):
# strinfo = ""
# strinfo = super(People,self).peopeinfo(self)
# strinfo = strinfo + self.profession


if __name__ == "__main__":
    fish = Animal("鲸鱼")
    print(fish.getkind())

    polorbear = Bear(kind ="北极熊", weight = 200, color ="")
    tedbear = Bear(kind ="泰迪熊", weight = "", color = "yellow")
    print(polorbear.getinfo())
    print(tedbear.getinfo())

    chinese = People("中国人","汉族")
    # 调用People类的方法
    print(chinese.getkind())
    # 调用父类的方法
    # print(chinese.super().getkind())
    # print(chinese.peopeinfo())
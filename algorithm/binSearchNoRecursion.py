# coding:utf-8
# 非递归的二分查找
sss = [1, 2, 3, 4, 5, 10, 22]


# 二分查找的话，有两种实现方式，一种就是递归的实现，一种就是非递归的模式
# 递归的话，那就是自己调用自己，而非递归的话，那就是一直循环，
# 直到对所有的情况，列举完成，才可
def binSearchWhile(mylist, key):
    start = 0
    end = len(mylist)
    while True:
        if len(mylist) == 0:
            print("列表的长度为0，查询不出来！")
            return -1;

        mid = int((start + end) / 2)
        print(mid)
        if key == mylist[mid]:
            print("查到了，" + str(key) + "的位置是： " + str(mid))
            return mid
        elif key < mylist[mid]:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == '__main__':
    print("123")
    binSearchWhile(sss, 88)

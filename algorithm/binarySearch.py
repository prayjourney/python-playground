# coding=utf-8
# 递归的二分查找
def binSearch(myarr, start, end, key):
    if (len(myarr) == 0):
        print("没有查找到关键字")
        return -1
    mid = (int)((start + end) / 2)

    if ((end - start == 1) and myarr[end] != key and myarr[start] != key):
        print("没有查找到关键字")
        return -1

    if (myarr[mid] == key):
        print(mid)
        return mid
    elif (myarr[mid] > key):
        return binSearch(myarr, start, mid, key)
    else:
        return binSearch(myarr, mid + 1, end, key)


if __name__ == '__main__':
    myarr = [1, 2, 1113]
    binSearch(myarr, 0, len(myarr) - 1, 1113)

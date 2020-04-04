"""
问题描述：有一座高度为n级的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶，求出一共有多少种走法。
"""


def upstairs(n):
    """
    第n个台阶的走法有F(n) = F(n-2) + F(n-1)这两种，存一次类推，那么边界的话就是，如果0个台阶，那就有0种走法
    如果第一个台阶，那就有1种走法，而第2个台阶，就有2种走法。
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return upstairs(n - 1) + upstairs(n - 2)


if __name__ == "__main__":
    print(upstairs(30))

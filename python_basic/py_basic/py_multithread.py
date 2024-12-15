"""
多线程
"""
import datetime
import threading
import time


def walk_dog(first_name, last_name):
    print(f"===start walking the dog at time: {datetime.datetime.now()}")
    time.sleep(8)
    print(f"You finish walking the dog {first_name} {last_name} at time: {datetime.datetime.now()}")


def take_out_trash():
    print(f"===start take_out_trash at time: {datetime.datetime.now()}")
    time.sleep(2)
    print(f"You take out the trash at time: {datetime.datetime.now()}")


def get_mail(who):
    print(f"===start get_mail at time: {datetime.datetime.now()}")
    time.sleep(4)
    print(f"You get the mail from {who} at time: {datetime.datetime.now()}")


# 下面的这3个任务是乱序的
chore1 = threading.Thread(target=walk_dog, args=('zg', 'duoduo')) #两个参数
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail, args=('zhangsan',)) #一个参数，后面的, 不能省略
chore3.start()

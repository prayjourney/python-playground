import datetime
import time

import pygame


def uset_time():
    time1 = time.time()   # 获取当前的时间戳
    print(time1)
    local_time_tuple = time.localtime(time1)
    print(local_time_tuple) # 获取结构性的时间
    print(local_time_tuple.tm_year)
    print(time.gmtime())     # 获取结构性的时间
    time.sleep(1) # 休眠1秒
    print("time is: ", time.strftime("%Y-%m-%d %H:%M:%S", local_time_tuple)) # 格式化时间
    print("time is: ", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


    # print(time1.strftime("%Y %m %d %H:%M:%S", time1))


def set_alarm(alarm_time):
    print(f"alarm time is {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True
    is_waking = False

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time and is_waking == False:
            is_waking = True
            print("wake up !!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            # is_running = False
            wake = input("are you waked? yes or no")
            if wake == "yes":
                is_running = False

        elif is_waking == False:
            time.sleep(1)
        else:
            print("do nothing")


if __name__ == '__main__':
    uset_time()
    # alarm_time = input("enter time (HH:MM:SS)")
    # set_alarm(alarm_time)

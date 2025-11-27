import datetime

def get_date_time():


    date = datetime.date(2022, 1,12) # 设置时间
    print(date)
    today = datetime.date.today() # 获取当天日期
    print(today)
    time = datetime.time(12, 20, 6)  # 设置时间
    print(time)
    now = datetime.datetime.now() # 获取当前时间
    print(now)

    now_format = now.strftime("%H:%M:%S %m-%d-%y") # 对象转换为字符串
    print(now_format)
    date_str = "2024-01-15"
    date_format = "%Y-%m-%d"
    parsed_date = datetime.datetime.strptime(date_str, date_format)  # 字符串转换为对象类型
    print("parsed date: ",parsed_date)

    date_time = datetime.datetime(2008, 12, 28, 1,10, 33)  # 设置时间
    print(date_time)


    next_day = today + datetime.timedelta(days=1)    # 时间运算
    print("next_day: ", next_day)


def get_time_without_mill():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("no mill: ", formatted_time)

    now_time = datetime.datetime.now()
    now_time_without_microseconds = now_time.replace(microsecond=0)
    print(now_time_without_microseconds)


if __name__ == '__main__':
    get_date_time()
    get_time_without_mill()
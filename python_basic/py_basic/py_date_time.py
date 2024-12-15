import  datetime

def get_date_time():


    date = datetime.date(2022, 1,12) # 设置时间
    print(date)
    today = datetime.date.today()
    print(today)
    time = datetime.time(12, 20, 6)  # 设置时间
    print(time)
    now = datetime.datetime.now()
    print(now)

    now_format = now.strftime("%H:%M:%S %m-%d-%y")
    print(now_format)

    date_time = datetime.datetime(2008, 12, 28, 1,10, 33)  # 设置时间
    print(date_time)


if __name__ == '__main__':
    get_date_time()
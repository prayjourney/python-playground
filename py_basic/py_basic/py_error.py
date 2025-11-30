try:
    # 尝试执行的代码
    num = int(input("请输入整数: "))
    result = 8 / num
    print(f"结果是: {result}")
except ValueError:
    print("输入的不是有效整数")
except ZeroDivisionError:
    print("除数不能为零")
except Exception as e:
    print(f"未知错误: {e}")
else:
    print("代码执行成功")  # 仅在无异常时执行
finally:
    print("无论是否异常都会执行")  # 用于资源清理

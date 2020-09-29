# 普通的方式启动，虽然是按照顺序的，但是越清楚越好
from PySide2.QtWidgets import QApplication
from pyside2.calcByClass import CalcSalary

if __name__ == "__main__":
    app = QApplication([])
    stats = CalcSalary()
    stats.window.show()
    app.exec_()

# 测试数据
# 薛蟠     4560 25
# 薛蝌     4460 25
# 薛宝钗   35776 23
# 薛宝琴   14346 18
# 王夫人   43360 45
# 王熙凤   24460 25
# 王子腾   55660 45
# 王仁     15034 65
# 尤二姐   5324 24
# 贾芹     5663 25
# 贾兰     13443 35
# 贾芸     4522 25
# 尤三姐   5905 22
# 贾珍     54603 35

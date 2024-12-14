from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])

# 定义一个槽函数，用于事件处理
def handleClick():
    print(123)


window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)
# 点击事件的响应
button.clicked.connect(handleClick)

window.show()

app.exec_()

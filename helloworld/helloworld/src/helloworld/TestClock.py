from tkinter import *
from time import strftime

class TestClock:
    mode = 'time'
    root = Tk()
    lb = Label()
    def startup(self):
        self.root.geometry('500x350+300+300')
        self.root.iconbitmap('E:/akkk/3_something/186d7984fbe8b82bf0b269d670bfa560.jpeg')
        self.root.title("C语言中文网出品")

        # 设置文本标签
        self.lb = Label(self.root, font=("微软雅黑", 50, "bold"), bg='#87CEEB', fg="#B452CD")
        self.lb.pack(anchor="center", fill="both", expand=1)

        # 定义一个mode标志
        mode = 'time'
        self.lb.bind("<Button>", self.mouseClick)
        # 调用showtime()函数
        self.showtime()
        # 显示窗口
        self.mainloop()

    # 定义显示时间的函数
    def showtime(self):
        if self.mode == 'time':
            # 时间格式化处理
            string = strftime("%H:%M:%S %p")
        else:
            string = strftime("%Y-%m-%d")
        self.lb.config(text=string)
        # 每隔 1秒钟执行time函数
        self.lb.after(1000, self.showtime)

    # 定义鼠标处理事件，点击时间切换为日期样式显示
    def mouseClick(self):
        if self.mode == 'time':
            # 点击切换mode样式为日期样式
            self.mode = 'date'
        else:
            self.mode = 'time'

    def mainloop(self):
        self.startup()


def main():
    return TestClock()

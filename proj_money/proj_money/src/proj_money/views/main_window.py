"""
主窗口视图类
"""
import toga
from toga.style import Pack


class MainWindow:
    def __init__(self, app):
        self.app = app
        self.window = toga.MainWindow(title=self.app.formal_name)
    
    def show(self):
        """显示窗口"""
        self.window.show()
    
    @property
    def content(self):
        """获取窗口内容"""
        return self.window.content
    
    @content.setter
    def content(self, value):
        """设置窗口内容"""
        self.window.content = value
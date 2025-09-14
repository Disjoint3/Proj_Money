"""
应用主入口点，初始化应用和主窗口
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from .controllers.main_controller import MainController
from .views.main_window import MainWindow


class ProjMoney(toga.App):
    def startup(self):
        """
        应用启动时调用，初始化主窗口和控制器
        """
        # 创建主窗口
        main_window = MainWindow(app=self)
        
        # 初始化主控制器
        self.main_controller = MainController(app=self, main_window=main_window)
        
        # 设置主窗口内容
        main_window.content = self.main_controller.get_main_content()
        
        # 显示主窗口
        main_window.show()


def main():
    """
    应用主函数，Briefcase会调用此函数启动应用
    """
    return ProjMoney('Proj Money', 'com.disjoint3.proj_money')
"""
主控制器，协调各个子控制器和视图
"""
import toga
from toga.style import Pack

from .expense_ctrl import ExpenseController
from .ledger_ctrl import LedgerController
from .other_ctrl import OtherController


class MainController:
    def __init__(self, app):
        self.app = app
        self.data_manager = app.data_manager

        # 初始化子控制器
        self.expense_ctrl = ExpenseController(self.app, self.data_manager)
        self.ledger_ctrl = LedgerController(self.app, self.data_manager)
        self.other_ctrl = OtherController(self.app, self.data_manager)

    def get_main_content(self):
        """创建主界面内容"""
        # 创建选项卡容器并直接初始化内容
        self.tab_content = toga.OptionContainer(
            content=[
                ('记账', self.expense_ctrl.get_view()),
                ('账本查看', self.ledger_ctrl.get_view()),
                ('其他', self.other_ctrl.get_view())
            ]
        )

        return self.tab_content

    def switch_to_tab(self, tab_index):
        """切换到指定选项卡"""
        self.tab_content.current_tab_index = tab_index
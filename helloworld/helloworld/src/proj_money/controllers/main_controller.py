"""
主控制器，协调各个子控制器和视图
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from ..models.data_manager import DataManager
from .expense_ctrl import ExpenseController
from .ledger_ctrl import LedgerController
from .other_ctrl import OtherController


class MainController:
    def __init__(self, app, main_window):
        self.app = app
        self.main_window = main_window
        self.data_manager = DataManager()
        
        # 初始化子控制器
        self.expense_ctrl = ExpenseController(self.app, self.data_manager)
        self.ledger_ctrl = LedgerController(self.app, self.data_manager)
        self.other_ctrl = OtherController(self.app, self.data_manager)
        
        # 当前活动视图
        self.current_view = None
    
    def get_main_content(self):
        """创建主界面内容"""
        # 创建选项卡容器
        self.tab_content = toga.OptionContainer(
            style=Pack(flex=1)
        )
        
        # 添加各功能选项卡
        self.tab_content.add('记账', self.expense_ctrl.get_view())
        self.tab_content.add('账本查看', self.ledger_ctrl.get_view())
        self.tab_content.add('其他', self.other_ctrl.get_view())
        
        return self.tab_content
    
    def switch_to_tab(self, tab_index):
        """切换到指定选项卡"""
        self.tab_content.current_tab_index = tab_index
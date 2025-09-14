"""
账本查看视图，构建账本查看界面
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class LedgerView:
    def __init__(self, controller):
        self.controller = controller
        self.build_view()
    
    def build_view(self):
        """构建账本查看界面"""
        # 显示模式选择
        self.view_mode = toga.Selection(
            items=['文本展示', '直观图示'],
            on_change=self.controller.on_view_mode_change,
            style=Pack(padding=5, flex=1)
        )

        # 分类方式选择
        self.category_mode = toga.Selection(
            items=['总的', '按种类分'],
            on_change=self.controller.on_category_mode_change,
            style=Pack(padding=5, flex=1)
        )
        
        # 内容显示区域
        self.content_area = toga.ScrollContainer(style=Pack(flex=1))
        
        # 构建主布局
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # 添加控制行
        control_row = toga.Box(style=Pack(direction=ROW))
        control_row.add(toga.Label('显示模式:', style=Pack(padding=5, width=100)))
        control_row.add(self.view_mode)
        control_row.add(toga.Label('分类方式:', style=Pack(padding=5, width=100)))
        control_row.add(self.category_mode)
        
        # 添加到主布局
        self.main_box.add(control_row)
        self.main_box.add(self.content_area)
    
    def get_view(self):
        """返回视图组件"""
        return self.main_box
    
    def update_content(self, content):
        """更新内容显示区域"""
        self.content_area.content = content
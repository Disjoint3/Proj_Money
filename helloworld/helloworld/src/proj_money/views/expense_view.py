"""
记账视图，构建记账界面
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ExpenseView:
    def __init__(self, controller):
        self.controller = controller
        self.build_view()
    
    def build_view(self):
        """构建记账界面"""
        # 金额输入
        self.amount_input = toga.NumberInput(style=Pack(padding=5))
        
        # 类别选择
        self.category_select = toga.Selection(
            items=self.controller.get_categories(),
            style=Pack(padding=5, flex=1)
        )
        
        # 备注输入
        self.note_input = toga.TextInput(
            placeholder='备注（可选）',
            style=Pack(padding=5, flex=1)
        )
        
        # 时间输入（可选）
        self.time_input = toga.TextInput(
            placeholder='YYYY-MM-DD HH:MM (可选)',
            style=Pack(padding=5, flex=1)
        )
        
        # 确认按钮
        self.confirm_button = toga.Button(
            '确认记录',
            on_press=self.controller.on_confirm_expense,
            style=Pack(padding=5)
        )
        
        # 构建主布局
        self.main_box = toga.Box(
            style=Pack(direction=COLUMN, padding=10)
        )
        
        # 添加输入行
        amount_row = toga.Box(style=Pack(direction=ROW))
        amount_row.add(toga.Label('金额:', style=Pack(padding=5, width=80)))
        amount_row.add(self.amount_input)
        
        category_row = toga.Box(style=Pack(direction=ROW))
        category_row.add(toga.Label('类别:', style=Pack(padding=5, width=80)))
        category_row.add(self.category_select)
        
        note_row = toga.Box(style=Pack(direction=ROW))
        note_row.add(toga.Label('备注:', style=Pack(padding=5, width=80)))
        note_row.add(self.note_input)
        
        time_row = toga.Box(style=Pack(direction=ROW))
        time_row.add(toga.Label('时间:', style=Pack(padding=5, width=80)))
        time_row.add(self.time_input)
        
        # 添加到主布局
        self.main_box.add(amount_row)
        self.main_box.add(category_row)
        self.main_box.add(note_row)
        self.main_box.add(time_row)
        self.main_box.add(self.confirm_button)
    
    def get_view(self):
        """返回视图组件"""
        return self.main_box
    
    def clear_inputs(self):
        """清空输入框"""
        self.amount_input.value = ''
        self.note_input.value = ''
        self.time_input.value = ''
    
    def get_input_values(self):
        """获取输入值"""
        return {
            'amount': float(self.amount_input.value) if self.amount_input.value else 0,
            'category': self.category_select.value,
            'note': self.note_input.value,
            'time': self.time_input.value if self.time_input.value else None
        }
"""
账本查看控制器，处理账本查看相关的业务逻辑
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from ..views.ledger_view import LedgerView


class LedgerController:
    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        self.view = LedgerView(self)
        self.view_mode = '文本展示'  # 默认显示模式
        self.category_mode = '总的'  # 默认分类方式
        
        # 初始化视图
        self.update_display()
    
    def get_view(self):
        """获取视图"""
        return self.view.get_view()
    
    def on_view_mode_change(self, widget):
        """处理显示模式变更事件"""
        self.view_mode = widget.value
        self.update_display()
    
    def on_category_mode_change(self, widget):
        """处理分类方式变更事件"""
        self.category_mode = widget.value
        self.update_display()
    
    def update_display(self):
        """更新显示内容"""
        if self.view_mode == '文本展示':
            content = self.create_text_display()
        else:
            content = self.create_chart_display()
        
        self.view.update_content(content)
    
    def create_text_display(self):
        """创建文本显示内容"""
        # 获取月度汇总
        summary = self.data_manager.get_monthly_summary()
        
        # 如果没有消费记录，显示提示信息
        if not summary['expenses']:
            return toga.Label("本月暂无消费记录", style=Pack(padding=10, font_size=16))

        # 创建表格
        table = toga.Table(
            headings=['ID', '金额', '类别', '时间', '备注'],
            data=[
                (exp['id'], f"{exp['amount']}元", exp['category'], 
                 exp['timestamp'][:16], exp.get('note', ''))
                for exp in summary['expenses']
            ],
            style=Pack(flex=1)
        )
        
        return table
    
    def create_chart_display(self):
        """创建图表显示内容"""
        # 获取月度汇总
        summary = self.data_manager.get_monthly_summary()

        # 如果没有消费记录，显示提示信息
        if not summary['expenses']:
            return toga.Label("本月暂无消费记录", style=Pack(padding=10, font_size=16))
        
        if self.category_mode == '总的':
            # 创建环形图
            # 这里使用标签模拟图表，实际应用中应使用图表库
            chart_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            
            total_label = toga.Label(
                f"总支出: {summary['total']}元", 
                style=Pack(padding=5, font_size=16, font_weight='bold')
            )
            
            chart_box.add(total_label)
            
            # 添加各类别占比
            for category, amount in summary['by_category'].items():
                percentage = (amount / summary['total'] * 100) if summary['total'] > 0 else 0
                category_label = toga.Label(
                    f"{category}: {amount}元 ({percentage:.1f}%)",
                    style=Pack(padding=2)
                )
                chart_box.add(category_label)
            
            return chart_box
        else:
            # 创建堆叠条形图
            # 这里使用标签模拟图表，实际应用中应使用图表库
            chart_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            
            # 添加各类别金额
            for category, amount in summary['by_category'].items():
                category_label = toga.Label(
                    f"{category}: {amount}元",
                    style=Pack(padding=5, font_size=14)
                )
                chart_box.add(category_label)
            
            return chart_box
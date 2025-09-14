"""
记账控制器，处理记账相关的业务逻辑
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from ..views.expense_view import ExpenseView


class ExpenseController:
    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        self.view = ExpenseView(self)
    
    def get_view(self):
        """获取视图"""
        return self.view.get_view()
    
    def get_categories(self):
        """获取消费类别列表"""
        return self.data_manager.get_categories()
    
    def on_confirm_expense(self, widget):
        """处理确认记账事件"""
        # 获取输入值
        input_values = self.view.get_input_values()
        
        # 验证输入
        if not input_values['amount'] or input_values['amount'] <= 0:
            self.show_message("错误", "请输入有效的金额")
            return
        
        if not input_values['category']:
            self.show_message("错误", "请选择消费类别")
            return
        
        # 处理时间输入
        timestamp = None
        if input_values['time']:
            try:
                from datetime import datetime
                timestamp = datetime.strptime(input_values['time'], '%Y-%m-%d %H:%M')
            except ValueError:
                self.show_message("错误", "时间格式不正确，请使用 YYYY-MM-DD HH:MM 格式")
                return
        
        # 创建消费记录
        expense_data = {
            'amount': input_values['amount'],
            'category': input_values['category'],
            'note': input_values['note']
        }
        
        if timestamp:
            expense_data['timestamp'] = timestamp.isoformat()
        
        # 保存记录
        expense_id = self.data_manager.add_expense(expense_data)
        
        # 检查是否超出预算
        self.check_budget_limit(input_values['category'], input_values['amount'])
        
        # 显示成功消息
        self.show_message("成功", f"记录已保存，ID: {expense_id}")
        
        # 清空输入
        self.view.clear_inputs()
    
    def check_budget_limit(self, category, amount):
        """检查是否超出预算限制"""
        monthly_limits = self.data_manager.get_monthly_limits()
        category_limit = monthly_limits.get(category, 0)
        total_limit = monthly_limits.get('total', 0)
        
        # 获取本月该类别总支出
        summary = self.data_manager.get_monthly_summary()
        category_total = summary['by_category'].get(category, 0)
        monthly_total = summary['total']
        
        # 检查是否超出限制
        category_exceeded = category_total > category_limit
        total_exceeded = monthly_total > total_limit
        
        if category_exceeded or total_exceeded:
            message = "警告：超出预算限制！\n"
            if category_exceeded:
                message += f"{category}类别: {category_total}元 / {category_limit}元\n"
            if total_exceeded:
                message += f"总计: {monthly_total}元 / {total_limit}元"
            
            self.show_message("预算警告", message)
    
    def show_message(self, title, message):
        """显示消息对话框"""
        self.app.main_window.info_dialog(title, message)
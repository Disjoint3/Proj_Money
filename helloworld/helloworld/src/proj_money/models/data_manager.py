"""
数据管理类，负责所有数据的存储和读取
使用二进制格式存储用户数据，JSON格式存储配置
"""
import os
import json
import pickle
from datetime import datetime
from ..utils.compat import get_data_path, ensure_data_dir


class DataManager:
    def __init__(self):
        # 确保数据目录存在
        self.data_dir = ensure_data_dir()
        self.expenses_file = os.path.join(self.data_dir, "expenses.dat")
        self.revoke_keys_file = os.path.join(self.data_dir, "revoke_keys.txt")
        self.config_file = os.path.join(self.data_dir, "config.json")

        # 加载默认配置
        self._load_default_config()

        # 加载用户数据
        self.expenses = self._load_expenses()
        self.revoke_keys = self._load_revoke_keys()

    def _load_default_config(self):
        """加载默认配置"""
        try:
            # 尝试加载用户配置
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 加载默认配置
            default_config_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.json')
            with open(default_config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            # 保存到用户目录
            self._save_config()

    def _save_config(self):
        """保存配置到文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def _load_expenses(self):
        """加载消费记录"""
        try:
            with open(self.expenses_file, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def save_expenses(self):
        """保存消费记录"""
        with open(self.expenses_file, 'wb') as f:
            pickle.dump(self.expenses, f)

    def _load_revoke_keys(self):
        """加载撤销密钥"""
        try:
            with open(self.revoke_keys_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            return []

    def save_revoke_keys(self):
        """保存撤销密钥"""
        with open(self.revoke_keys_file, 'w', encoding='utf-8') as f:
            for key in self.revoke_keys:
                f.write(key + '\n')

    def add_expense(self, expense_data):
        """添加消费记录"""
        # 生成唯一ID
        expense_id = len(self.expenses) + 1
        expense_data['id'] = expense_id
        expense_data['timestamp'] = datetime.now().isoformat()

        self.expenses.append(expense_data)
        self.save_expenses()
        return expense_id

    def revoke_expense(self, expense_id, revoke_key):
        """撤销消费记录"""
        if revoke_key not in self.revoke_keys:
            return False, "撤销密钥不正确"

        # 查找并移除记录
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                self.expenses.pop(i)
                self.save_expenses()
                return True, "撤销成功"

        return False, "未找到对应的消费记录"

    def generate_revoke_key(self):
        """生成新的撤销密钥"""
        import secrets
        import string

        alphabet = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(alphabet) for _ in range(16))
        self.revoke_keys.append(key)
        self.save_revoke_keys()
        return key

    def get_monthly_summary(self, year=None, month=None):
        """获取月度消费汇总"""
        now = datetime.now()
        year = year or now.year
        month = month or now.month

        monthly_expenses = [
            exp for exp in self.expenses
            if self._is_same_month(exp['timestamp'], year, month)
        ]

        # 按类别汇总
        category_totals = {}
        for exp in monthly_expenses:
            category = exp['category']
            amount = exp['amount']
            category_totals[category] = category_totals.get(category, 0) + amount

        # 计算总支出
        total = sum(category_totals.values())

        return {
            'total': total,
            'by_category': category_totals,
            'expenses': monthly_expenses
        }

    def _is_same_month(self, timestamp, year, month):
        """检查时间戳是否在指定年月"""
        dt = datetime.fromisoformat(timestamp)
        return dt.year == year and dt.month == month

    def get_categories(self):
        """获取所有消费类别"""
        return self.config.get('categories', [])

    def get_monthly_limits(self):
        """获取月度消费限制"""
        return self.config.get('monthly_limits', {})

    def get_app_info(self):
        """获取应用信息"""
        return {
            'version': self.config.get('version', '1.0.0'),
            'build_date': self.config.get('build_date', '未知'),
            'author': self.config.get('author', 'disjoint3（LYL）'),
            'acknowledgements': self.config.get('acknowledgements', ['briefcase', 'toga'])
        }
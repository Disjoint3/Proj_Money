"""
消费记录模型类
"""
from datetime import datetime


class Expense:
    def __init__(self, amount, category, timestamp=None, note=""):
        self.amount = amount
        self.category = category
        self.timestamp = timestamp or datetime.now()
        self.note = note
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            'amount': self.amount,
            'category': self.category,
            'timestamp': self.timestamp.isoformat(),
            'note': self.note
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建对象"""
        return cls(
            amount=data.get('amount', 0),
            category=data.get('category', '其他'),
            timestamp=datetime.fromisoformat(data.get('timestamp', datetime.now().isoformat())),
            note=data.get('note', '')
        )
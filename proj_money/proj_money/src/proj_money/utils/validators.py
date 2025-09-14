"""
数据验证工具函数
"""


def validate_amount(amount):
    """验证金额是否有效"""
    try:
        amount_float = float(amount)
        return amount_float > 0
    except (ValueError, TypeError):
        return False


def validate_date(date_string):
    """验证日期字符串是否有效"""
    from datetime import datetime
    try:
        datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        return True
    except (ValueError, TypeError):
        return False
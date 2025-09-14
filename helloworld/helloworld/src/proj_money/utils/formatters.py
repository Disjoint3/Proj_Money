"""
数据格式化工具函数
"""


def format_currency(amount):
    """格式化货币金额"""
    return f"{amount:.2f}元"


def format_date(date_string):
    """格式化日期字符串"""
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M')
    except (ValueError, AttributeError):
        return date_string
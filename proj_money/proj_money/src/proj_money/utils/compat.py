"""
平台兼容性工具函数，处理Windows和Android的差异
"""
import os
import sys
from pathlib import Path


def get_data_path():
    """
    获取跨平台的数据存储路径
    Windows: %APPDATA%/Proj_Money
    Android: 应用专用存储目录
    """
    if sys.platform == 'android':
        from android.storage import app_storage_path
        return app_storage_path()
    else:
        # Windows和其他平台
        app_data = os.getenv('APPDATA') or os.path.expanduser('~')
        return os.path.join(app_data, 'Proj_Money')


def ensure_data_dir():
    """确保数据目录存在"""
    data_path = get_data_path()
    os.makedirs(data_path, exist_ok=True)
    return data_path


def get_icon_path(icon_name):
    """
    获取图标路径，处理Android的资源访问方式
    """
    if sys.platform == 'android':
        # Android上图标可能需要特殊处理
        # 这里假设图标放在应用的资源目录中
        return f"resources/icons/{icon_name}"
    else:
        # 其他平台直接使用文件路径
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        return os.path.join(base_dir, 'resources', 'icons', icon_name)
"""
配置模型类
"""
import json
import os
from ..utils.compat import get_data_path


class Config:
    def __init__(self):
        self.config_path = os.path.join(get_data_path(), "config.json")
        self.config = self._load_config()
    
    def _load_config(self):
        """加载配置"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 返回默认配置
            return {
                'version': '1.0.0',
                'build_date': '2023-11-01',
                'author': 'disjoint3（LYL）',
                'acknowledgements': ['briefcase', 'toga'],
                'categories': ['餐饮', '交通', '购物', '娱乐', '学习', '医疗', '其他'],
                'monthly_limits': {
                    '餐饮': 1000, '交通': 500, '购物': 1500, 
                    '娱乐': 800, '学习': 300, '医疗': 200, '其他': 500,
                    'total': 5000
                }
            }
    
    def save(self):
        """保存配置"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置值"""
        self.config[key] = value
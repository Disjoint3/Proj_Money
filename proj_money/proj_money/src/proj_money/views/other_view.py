"""
其他视图，构建其他信息界面
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class OtherView:
    def __init__(self, controller):
        self.controller = controller
        self.build_view()
    
    def build_view(self):
        """构建其他信息界面"""
        # 应用信息
        app_info = self.controller.get_app_info()
        
        # 创建信息标签
        info_labels = [
            toga.Label(f"作者: {app_info.get('author', 'disjoint3（LYL）')}", style=Pack(margin=5)),
            toga.Label(f"版本: {app_info.get('version', '1.0.0')}", style=Pack(margin=5)),
            toga.Label(f"构建日期: {app_info.get('build_date', '未知')}", style=Pack(margin=5)),
            toga.Label(f"鸣谢: {', '.join(app_info.get('acknowledgements', ['briefcase', 'toga']))}", style=Pack(margin=5)),
        ]
        
        # 配置信息标题
        config_title = toga.Label("当前配置:", style=Pack(margin=10, font_weight='bold'))
        
        # 配置信息
        config_info = self.controller.get_config_info()
        config_labels = []
        
        for category, limit in config_info.get('monthly_limits', {}).items():
            if category != 'total':
                config_labels.append(toga.Label(f"{category}: {limit}元", style=Pack(margin=2)))
        
        config_labels.append(toga.Label(f"总计: {config_info.get('monthly_limits', {}).get('total', 0)}元", 
                                      style=Pack(margin=5, font_weight='bold')))
        
        # 构建主布局
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # 添加信息标签
        for label in info_labels:
            self.main_box.add(label)
        
        self.main_box.add(config_title)
        
        for label in config_labels:
            self.main_box.add(label)
    
    def get_view(self):
        """返回视图组件"""
        return self.main_box
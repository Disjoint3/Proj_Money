"""
其他控制器，处理其他信息相关的业务逻辑
"""
from ..views.other_view import OtherView


class OtherController:
    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        self.view = OtherView(self)
    
    def get_view(self):
        """获取视图"""
        return self.view.get_view()
    
    def get_app_info(self):
        """获取应用信息"""
        return self.data_manager.get_app_info()
    
    def get_config_info(self):
        """获取配置信息"""
        return {
            'categories': self.data_manager.get_categories(),
            'monthly_limits': self.data_manager.get_monthly_limits()
        }
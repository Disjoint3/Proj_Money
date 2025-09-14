"""
撤销记录控制器，处理撤销相关的业务逻辑
"""
import toga


class RevokeController:
    def __init__(self, app, data_manager):
        self.app = app
        self.data_manager = data_manager
        from ..views.revoke_dialog import RevokeDialog
        self.dialog = RevokeDialog(self)

    def show_dialog(self):
        """显示撤销对话框"""
        self.dialog.clear_inputs()
        self.dialog.show()

    def on_generate_key(self, widget):
        """处理生成新密钥事件"""
        try:
            key = self.data_manager.generate_revoke_key()
            self.dialog.set_generated_key(key)

            # 显示成功消息
            self.app.main_window.info_dialog(
                "密钥生成成功",
                f"已生成新撤销密钥: {key}\n密钥已保存到文件，请妥善保管。"
            )
        except Exception as e:
            self.app.main_window.error_dialog("错误", f"生成密钥时发生错误: {str(e)}")

    def on_confirm_revoke(self, widget):
        """处理确认撤销事件"""
        # 获取输入值
        input_values = self.dialog.get_input_values()

        # 验证输入
        if not input_values['expense_id']:
            self.dialog.set_result(False, "请输入条目ID")
            return

        if not input_values['revoke_key']:
            self.dialog.set_result(False, "请输入撤销密钥")
            return

        try:
            expense_id = int(input_values['expense_id'])
        except ValueError:
            self.dialog.set_result(False, "条目ID必须是数字")
            return

        # 执行撤销操作
        success, message = self.data_manager.revoke_expense(expense_id, input_values['revoke_key'])
        self.dialog.set_result(success, message)

        # 如果撤销成功，显示额外提示
        if success:
            self.app.main_window.info_dialog("撤销成功", f"已成功撤销条目ID为 {expense_id} 的记录")
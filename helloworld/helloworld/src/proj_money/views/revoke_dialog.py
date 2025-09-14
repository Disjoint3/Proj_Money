"""
撤销记录对话框视图
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class RevokeDialog:
    def __init__(self, controller):
        self.controller = controller
        self.dialog = None
        self.build_dialog()

    def build_dialog(self):
        """构建撤销对话框"""
        # 条目ID输入
        self.id_input = toga.TextInput(placeholder='请输入要撤销的条目ID', style=Pack(flex=1, margin=5))

        # 撤销密钥输入
        self.key_input = toga.TextInput(placeholder='请输入撤销密钥', style=Pack(flex=1, margin=5))

        # 生成新密钥按钮
        self.generate_key_btn = toga.Button(
            '生成新的撤销密钥',
            on_press=self.controller.on_generate_key,
            style=Pack(margin=5)
        )

        # 确认撤销按钮
        self.confirm_btn = toga.Button(
            '确认撤销',
            on_press=self.controller.on_confirm_revoke,
            style=Pack(margin=5)
        )

        # 结果显示标签
        self.result_label = toga.Label('', style=Pack(margin=5, color='black'))

        # 构建对话框内容
        content = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # 添加ID输入行
        id_row = toga.Box(style=Pack(direction=ROW))
        id_row.add(toga.Label('条目ID:', style=Pack(width=100, margin=5)))
        id_row.add(self.id_input)

        # 添加密钥输入行
        key_row = toga.Box(style=Pack(direction=ROW))
        key_row.add(toga.Label('撤销密钥:', style=Pack(width=100, margin=5)))
        key_row.add(self.key_input)

        # 添加到主内容
        content.add(id_row)
        content.add(key_row)
        content.add(self.generate_key_btn)
        content.add(self.confirm_btn)
        content.add(self.result_label)

        # 创建对话框
        self.dialog = toga.Window(
            title='撤销记录',
            size=(400, 300),
            position=(100, 100)
        )
        self.dialog.content = content

    def show(self):
        """显示对话框"""
        self.dialog.show()

    def hide(self):
        """隐藏对话框"""
        self.dialog.hide()

    def clear_inputs(self):
        """清空输入框"""
        self.id_input.value = ''
        self.key_input.value = ''
        self.result_label.text = ''

    def set_result(self, success, message):
        """设置结果显示"""
        if success:
            self.result_label.style.color = 'green'
        else:
            self.result_label.style.color = 'red'
        self.result_label.text = message

    def get_input_values(self):
        """获取输入值"""
        return {
            'expense_id': self.id_input.value,
            'revoke_key': self.key_input.value
        }

    def set_generated_key(self, key):
        """设置生成的密钥"""
        self.key_input.value = key
        self.result_label.text = f'已生成新密钥: {key}'
        self.result_label.style.color = 'blue'
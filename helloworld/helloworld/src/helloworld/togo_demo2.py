import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


class togo_demo2(toga.App):
    def startup(self):
        c_box = toga.Box()
        f_box = toga.Box()
        main_box = toga.Box()

        c_input = toga.TextInput(readonly=True)
        f_input = toga.TextInput()

        c_label = toga.Label("Celsius", style=Pack(text_align=LEFT))
        f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT))
        join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

        def calculate(widget):
            try:
                c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
            except ValueError:
                c_input.value = "???"

        button = toga.Button("Calculate", on_press=calculate)

        f_box.add(f_input)
        f_box.add(f_label)

        c_box.add(join_label)
        c_box.add(c_input)
        c_box.add(c_label)

        main_box.add(f_box)
        main_box.add(c_box)
        main_box.add(button)

        main_box.style.update(direction=COLUMN, margin=10, gap=10)
        f_box.style.update(direction=ROW, gap=10)
        c_box.style.update(direction=ROW, gap=10)

        c_input.style.update(flex=1)
        f_input.style.update(flex=1, margin_left=210)
        c_label.style.update(width=100)
        f_label.style.update(width=100)
        join_label.style.update(width=200)

        button.style.update(margin_top=5)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return togo_demo2("toga_demo2","org.beeware.toga.examples.tutorial")
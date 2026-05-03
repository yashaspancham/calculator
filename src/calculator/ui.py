import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.calculator.widgets.display import create_display
from src.calculator.widgets.keyboard import create_keyboard
from src.calculator.engine import calculate_expression, square_root, square, negate, extract_last_number


class Calculator(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Calculator")
                self.init_set_up()

        def init_set_up(self):
                central = QWidget()
                outer_layout = QVBoxLayout()
                outer_layout.setAlignment(Qt.AlignCenter)

                calculator_box = QWidget()
                calculator_box.setFixedSize(400, 450)
                main_layout = QVBoxLayout()

                self.display = create_display()
                main_layout.addWidget(self.display)

                self.keyboard, self.buttons = create_keyboard()
                main_layout.addWidget(self.keyboard)

                for text, button in self.buttons.items():
                        button.clicked.connect(lambda checked, t=text: self.button_clicked(t))

                calculator_box.setLayout(main_layout)
                outer_layout.addWidget(calculator_box)
                central.setLayout(outer_layout)
                self.setCentralWidget(central)

        def set_text(self, text) -> None:
                self.display.setText(str(text))

        def button_clicked(self, value) -> None:
                current = self.display.text()

                if value == "=":
                        self.set_text(calculate_expression(current))
                elif value == "√":
                        prefix, num = extract_last_number(current)
                        self.set_text(prefix + str(square_root(num)))
                elif value == "x²":
                        prefix, num = extract_last_number(current)
                        self.set_text(prefix + str(square(num)))
                elif value == "±":
                        prefix, num = extract_last_number(current)
                        self.set_text(prefix + str(negate(num)))
                elif value == "⌫":
                        self.set_text(current[:-1])
                elif value == "C":
                        self.set_text('0')
                elif current in ("0", "Welcome", "Error"):
                        self.set_text(value)
                else:
                        self.set_text(current + value)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Calculator()
        window.show()
        sys.exit(app.exec_())
from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget
from src.calculator.theme import theme


def create_keyboard():
        container = QWidget()
        grid = QGridLayout()
        grid.setSpacing(theme['general']['spacing'])
        container.setLayout(grid)
        btns = {}
        buttons = [
                ("C",  0, 0), ("⌫",  0, 1), ("%",  0, 2), ("÷", 0, 3),
                ("√",  1, 0), ("x²", 1, 1), ("±",  1, 2), ("×", 1, 3),
                ("7",  2, 0), ("8",  2, 1), ("9",  2, 2), ("−", 2, 3),
                ("4",  3, 0), ("5",  3, 1), ("6",  3, 2), ("+", 3, 3),
                ("1",  4, 0), ("2",  4, 1), ("3",  4, 2), ("=", 4, 3),
                ("0",  5, 0), (".",  5, 2),
        ]

        for text, row, col in buttons:
                button = QPushButton(text)
                grid.setRowStretch(row, 0)
                button.setMinimumHeight(60)
                if text in ["+", "−", "×", "÷"]:
                        style = theme["buttons"]["operator"]
                elif text == "=":
                        style = theme["buttons"]["equal"]
                elif text == "C":
                        style = theme["buttons"]["clear"]
                else:
                        style = theme["buttons"]["number"]

                button.setStyleSheet(keyboard_style(style))

                if text == "0":
                        grid.addWidget(button, row, col, 1, 2)
                else:
                        grid.addWidget(button, row, col)
                btns[text] = button

        
        return container, btns


def keyboard_style(style):
        return f"""
                QPushButton {{
                        background-color: {style["background"]};
                        color: {style["text_color"]};
                        border: {style["border"]};
                        border-radius: {theme["general"]["button_radius"]}px;
                        font-size: {theme["general"]["button_font_size"]}px;
                        padding: {theme["general"]["button_padding"]}px;
                }}
                QPushButton:hover {{
                        background-color: {style["hover"]}
                }}
                QPushButton:pressed {{
                        background-color: {style["pressed"]}
                        }}
                """
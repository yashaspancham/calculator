from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
from src.calculator.theme import theme

def create_display():
        
        display = QLineEdit()

        display.setReadOnly(True)
        display.setAlignment(Qt.AlignRight)
        display.setText("Welcome")
        display.setFixedHeight(70)

        display.setStyleSheet(display_style())

        return display



def display_style() -> str:
        return f"""
                QLineEdit{{
                        background-color: {theme["display"]['background']};
                        border-radius: {theme["display"]['border_radius']}px;
                        color: {theme["display"]['text_color']};
                        border: {theme["display"]['border']};
                        padding: {theme["display"]["padding"]}px;
                        font-size: {theme["display"]["font_size"]}px;
                }}
        """
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QMessageBox, QAction,
    QGroupBox, QFormLayout, QComboBox, QFrame
)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def status_color(status):
    if status == "Underweight":
        return "#3b82f6"
    if status == "Normal":
        return "#22c55e"
    if status == "Overweight":
        return "#f59e0b"
    return "#ef4444"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.resize(720, 420)
        self.setMinimumSize(720, 420)

        self.metric_radio = QRadioButton("Metric")
        self.imperial_radio = QRadioButton("Imperial")
        self.metric_radio.setChecked(True)

        self.units_group = QButtonGroup()
        self.units_group.addButton(self.metric_radio)
        self.units_group.addButton(self.imperial_radio)

        top = QHBoxLayout()
        title = QLabel("BMI Calculator")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        subtitle = QLabel("Quickly calculate your Body Mass Index")
        subtitle.setStyleSheet("color:#6b7280;")
        title_col = QVBoxLayout()
        title_col.addWidget(title)
        title_col.addWidget(subtitle)
        title_col.addStretch(1)

        units_box = QGroupBox("Units")
        units_row = QHBoxLayout()
        units_row.addWidget(self.metric_radio)
        units_row.addWidget(self.imperial_radio)
        units_box.setLayout(units_row)

        top.addLayout(title_col)
        top.addWidget(units_box)

        self.weight_input = QLineEdit()
        self.height_input = QLineEdit()

        self.weight_input.setPlaceholderText("e.g., 70")
        self.height_input.setPlaceholderText("e.g., 1.75")

        val = QDoubleValidator(0.0, 1000000.0, 6)
        val.setNotation(QDoubleValidator.StandardNotation)
        self.weight_input.setValidator(val)
        self.height_input.setValidator(val)

        self.height_mode = QComboBox()
        self.height_mode.addItems(["m", "cm"])
        self.height_mode.setCurrentText("m")

        form = QFormLayout()
        self.weight_label = QLabel("Weight (kg)")
        self.height_label = QLabel("Height")
        w_row = QHBoxLayout()
        w_row.addWidget(self.weight_input)
        w_unit = QLabel("kg")
        w_unit.setStyleSheet("color:#6b7280;")
        w_row.addWidget(w_unit)
        w_wrap = QWidget()
        w_wrap.setLayout(w_row)

        h_row = QHBoxLayout()
        h_row.addWidget(self.height_input)
        h_row.addWidget(self.height_mode)
        h_wrap = QWidget()
        h_wrap.setLayout(h_row)

        form.addRow(self.weight_label, w_wrap)
        form.addRow(self.height_label, h_wrap)

        inputs_box = QGroupBox("Input")
        inputs_box.setLayout(form)

        self.calc_btn = QPushButton("Calculate")
        self.calc_btn.setFixedHeight(42)
        self.calc_btn.setCursor(Qt.PointingHandCursor)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setFixedHeight(42)
        self.clear_btn.setCursor(Qt.PointingHandCursor)

        btns = QHBoxLayout()
        btns.addWidget(self.calc_btn, 3)
        btns.addWidget(self.clear_btn, 1)

        left = QVBoxLayout()
        left.addWidget(inputs_box)
        left.addLayout(btns)
        left.addStretch(1)

        self.result_bmi = QLabel("-")
        self.result_bmi.setFont(QFont("Segoe UI", 28, QFont.Bold))
        self.result_bmi.setAlignment(Qt.AlignCenter)

        self.result_status = QLabel("Enter values and press Calculate")
        self.result_status.setAlignment(Qt.AlignCenter)
        self.result_status.setStyleSheet("color:#6b7280; font-size:14px;")

        hint = QLabel("Tip: In Metric you can enter height in meters or centimeters.")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet("color:#9ca3af;")

        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout()
        card_layout.addWidget(QLabel("Your BMI"))
        card_layout.itemAt(0).widget().setAlignment(Qt.AlignCenter)
        card_layout.itemAt(0).widget().setStyleSheet("color:#6b7280; font-size:14px;")
        card_layout.addSpacing(6)
        card_layout.addWidget(self.result_bmi)
        card_layout.addWidget(self.result_status)
        card_layout.addSpacing(10)
        card_layout.addWidget(hint)
        card.setLayout(card_layout)

        right = QVBoxLayout()
        right.addWidget(card)
        right.addStretch(1)

        main_row = QHBoxLayout()
        main_row.addLayout(left, 2)
        main_row.addLayout(right, 3)

        root = QVBoxLayout()
        root.addLayout(top)
        root.addSpacing(10)
        root.addLayout(main_row)

        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            QMainWindow { background: #0b1220; }
            QLabel { color: #e5e7eb; font-family: "Segoe UI"; }
            QGroupBox {
                color: #e5e7eb;
                border: 1px solid #22304a;
                border-radius: 14px;
                margin-top: 10px;
                padding: 12px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                color: #9ca3af;
            }
            QLineEdit {
                background: #0f1a2e;
                border: 1px solid #22304a;
                border-radius: 10px;
                padding: 10px;
                color: #e5e7eb;
                font-size: 14px;
            }
            QLineEdit:focus { border: 1px solid #3b82f6; }
            QComboBox {
                background: #0f1a2e;
                border: 1px solid #22304a;
                border-radius: 10px;
                padding: 8px 10px;
                color: #e5e7eb;
            }
            QPushButton {
                background: #2563eb;
                border: none;
                border-radius: 12px;
                color: white;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover { background: #1d4ed8; }
            QPushButton:pressed { background: #1e40af; }
            QPushButton#clearBtn { background: #334155; }
            QFrame#card {
                background: #0f1a2e;
                border: 1px solid #22304a;
                border-radius: 18px;
                padding: 18px;
            }
            QRadioButton { color:#e5e7eb; }
        """)

        self.clear_btn.setObjectName("clearBtn")

        self.calc_btn.clicked.connect(self.calculate)
        self.clear_btn.clicked.connect(self.clear_fields)
        self.weight_input.returnPressed.connect(self.calculate)
        self.height_input.returnPressed.connect(self.calculate)
        self.units_group.buttonClicked.connect(self.update_ui)
        self.height_mode.currentIndexChanged.connect(self.update_ui)

        self.build_menu()
        self.update_ui()

    def build_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        clear_action = QAction("Clear", self)
        clear_action.setShortcut("Ctrl+L")
        clear_action.triggered.connect(self.clear_fields)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(clear_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")
        how_action = QAction("How to use", self)
        how_action.triggered.connect(self.show_help)
        help_menu.addAction(how_action)

    def update_ui(self):
        if self.metric_radio.isChecked():
            self.weight_label.setText("Weight (kg)")
            self.height_label.setText("Height")
            self.height_mode.setEnabled(True)
        else:
            self.weight_label.setText("Weight (lb)")
            self.height_label.setText("Height (in)")
            self.height_mode.setEnabled(False)
            self.height_mode.setCurrentText("m")

    def get_float(self, line_edit):
        t = line_edit.text().strip().replace(",", ".")
        return float(t)

    def calculate(self):
        try:
            w = self.get_float(self.weight_input)
            h = self.get_float(self.height_input)
            if w <= 0 or h <= 0:
                raise ValueError()

            if self.metric_radio.isChecked():
                if self.height_mode.currentText() == "cm":
                    h = h / 100.0
            else:
                w = w * 0.45359237
                h = h * 0.0254

            if h <= 0:
                raise ValueError()

            bmi = w / (h * h)
            st = bmi_status(bmi)

            self.result_bmi.setText(f"{bmi:.2f}")
            self.result_status.setText(st)
            self.result_status.setStyleSheet(f"color:{status_color(st)}; font-size:16px; font-weight:700;")
        except Exception:
            QMessageBox.warning(self, "Invalid input", "Enter positive numbers for weight and height.")
            self.result_bmi.setText("-")
            self.result_status.setText("Enter values and press Calculate")
            self.result_status.setStyleSheet("color:#6b7280; font-size:14px;")

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_bmi.setText("-")
        self.result_status.setText("Enter values and press Calculate")
        self.result_status.setStyleSheet("color:#6b7280; font-size:14px;")
        self.weight_input.setFocus()

    def show_help(self):
        QMessageBox.information(
            self,
            "Help",
            "Metric:\n- Weight in kg\n- Height in m or cm\n\nImperial:\n- Weight in lb\n- Height in inches\n\nPress Calculate or Enter."
        )

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
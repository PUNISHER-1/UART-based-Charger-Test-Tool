import sys
import csv
import re
from datetime import datetime, timezone
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QMessageBox

connector_id = 0
current_time_utc = datetime.now(timezone.utc)

class ValueThread(QThread):
    current_data = pyqtSignal(dict)
    voltage_data = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
        self.window = QMainWindow()
        self.current_import_matches = []
        self.voltage_outlet_matches = []

        self.initUI()

    def initUI(self):
        self.window.setWindowTitle("CURRENT & VOLTAGE")

        self.gun1_btn = QPushButton("GUN 1 values", self.window)
        self.gun1_btn.clicked.connect(self.gun1_values)

        self.gun2_btn = QPushButton("GUN 2 values", self.window)
        self.gun2_btn.clicked.connect(self.gun2_values)

        self.ok_btn = QPushButton("OKAY", self.window)
        self.ok_btn.clicked.connect(self.ok_send)

        self.log_text = QTextEdit(self.window)
        self.log_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.gun1_btn)
        layout.addWidget(self.gun2_btn)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.log_text)

        container = QWidget()
        container.setLayout(layout)
        self.window.setCentralWidget(container)

    def gun1_values(self):
        self.running = True
        self.start()
        connector_id = 1
        formatted_time = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.xxx(connector_id, formatted_time)

    def gun2_values(self):
        self.running = True
        self.start()
        connector_id = 2
        formatted_time = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.xxx(connector_id, formatted_time)       

    def ok_send(self):
        self.current_data.emit({"gun" : connector_id,
                                "current" : self.current_import_matches})
        self.voltage_data.emit({"gun" : connector_id,
                                "current" : self.voltage_outlet_matches})

    def xxx(self, connector_id, formatted_time):
        filename = "data.csv"  
        extracted_data = ""
        capturing = False
        found_timestamp = False

        target_timestamp = "2024-04-12T04:30:16Z"
        main_extracted_data = ""

        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                timestamp, data = row
                data = data.strip()
                if f'"connectorId":	{connector_id},' in data:
                    # print(connector_id)
                    capturing = True

                if capturing:
                    extracted_data += data + " "
                    if target_timestamp in extracted_data:
                        found_timestamp = True  # Indicate that the target timestamp was found

                    if found_timestamp:
                        main_extracted_data += data + " "
                        if '"unit": "Celsius"' in data:
                            break  # Stop capturing after the Celsius unit is found

        main_extracted_data = ' '.join(main_extracted_data.split())
 
        current_import_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Current\.Import", "location": "Outlet", "unit": "A" \}'
        voltage_outlet_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Voltage", "location": "Outlet", "unit": "V" \}'
        
        self.current_import_matches = re.findall(current_import_pattern, main_extracted_data)
        self.voltage_outlet_matches = re.findall(voltage_outlet_pattern, main_extracted_data)
        
        x = ("Current Value of GUN "+ f'{connector_id} : ' + ", ".join(self.current_import_matches))
        y = ("Voltage Value of GUN "+ f'{connector_id} : ' + ", ".join(self.voltage_outlet_matches))

        self.log_text.append(x)
        self.log_text.append(y)

        print(x)
        print(y)

    def execute(self):
        self.window.show()
        if not QApplication.instance():
            sys.exit(self.app.exec_())
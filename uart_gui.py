import sys
import time
import csv
import serial
import re
import os
from datetime import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QMessageBox

class UartThread(QThread):
    chargerSn = pyqtSignal(dict)
    message_signal = pyqtSignal(str)
    connected_signal = pyqtSignal()
    disconnected_signal = pyqtSignal()
    finished_signal = pyqtSignal()
    keyword_signal = pyqtSignal(dict)

    def __init__(self, port, baudrate, data_csv_path):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.data_csv_path = data_csv_path
        self.running = False
        self.local_content = {}

        # UI initialization
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
        self.window = QMainWindow()
        self.initUI()

    def initUI(self):
        self.window.setWindowTitle("UART Reader")

        self.start_button = QPushButton("Start Reading", self.window)
        self.start_button.clicked.connect(self.start_reading)

        self.terminate_button = QPushButton("Terminate Session", self.window)
        self.terminate_button.clicked.connect(self.terminate_session)
        self.terminate_button.setEnabled(False)

        self.log_text = QTextEdit(self.window)
        self.log_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.terminate_button)
        layout.addWidget(self.log_text)

        container = QWidget()
        container.setLayout(layout)
        self.window.setCentralWidget(container)

    def start_reading(self):
        self.running = True
        self.start()
        self.start_button.setEnabled(False)
        self.terminate_button.setEnabled(True)

    def terminate_session(self):
        self.running = False
        self.start_button.setEnabled(True)
        self.terminate_button.setEnabled(False)

    def run(self):
        self.running = True
        # previous_timestamp = None
        try:
                ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=1)
                self.connected_signal.emit()
                print(f"Connected to {self.port} at {self.baudrate} baud.")
                with open(self.data_csv_path, 'w', newline='', buffering=1) as file:
                    writer = csv.writer(file)
                    writer.writerow(['Timestamp', 'Data'])
                    while self.running:
                        if ser.in_waiting > 0:
                            data = ser.readline().decode('utf-8').rstrip()
                            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                            if not data:
                                continue
                            writer.writerow([current_timestamp, data])
                            print(data)
                            self.check_for_keywords(data) 
                            file.flush()
        except serial.SerialException as e:
            self.message_signal.emit(f"Serial exception: {e}")
        finally:
            self.disconnected_signal.emit()
            self.finished_signal.emit()

    def check_for_keywords(self, data):
        keywords = ['chargePointSerialNumber', 'chargePointModel']
        found_any = False  
        for keyword in keywords:
            if keyword in data:
                match = re.search(f'"{keyword}":\\s*"(.*?)"', data, re.IGNORECASE)
                if match:
                    self.local_content[keyword] = match.group(1)
                    self.message_signal.emit(f"{keyword} found: {self.local_content[keyword]}")
                    found_any = True     
        time.sleep(4)             
        if found_any:   
            print(self.local_content)
            self.chargerSn.emit(self.local_content)  
            
    def update_log(self, message):
        self.log_text.append(message)

    def display_keywords(self, keywords):
        for key, value in keywords.items():
            self.log_text.append(f"{key}: {value}")

    def show_connected_message(self):
        self.log_text.append("UART device connected.")

    def show_disconnected_message(self):
        self.log_text.append("UART device disconnected.")

    def show_completion_dialog(self):
        QMessageBox.information(self.window, "Processing Complete", "UART data processing is complete.")
        self.start_button.setEnabled(True)
        self.terminate_button.setEnabled(False)

    def execute(self):
        # Connect signals
        self.message_signal.connect(self.update_log)
        self.keyword_signal.connect(self.display_keywords)
        self.connected_signal.connect(self.show_connected_message)
        self.disconnected_signal.connect(self.show_disconnected_message)
        self.finished_signal.connect(self.show_completion_dialog)

        self.window.show()
        if not QApplication.instance():
            sys.exit(self.app.exec_())

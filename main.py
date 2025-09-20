global context
context = {}
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from generate_t import GenerateThread
from uart_gui import UartThread
from values import ValueThread

class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

    # PROGRESS  BAR #############################
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 470, 461, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.l_processing = QtWidgets.QLabel(self.centralwidget)
        self.l_processing.setGeometry(QtCore.QRect(60, 510, 421, 20))
        self.l_processing.setAlignment(QtCore.Qt.AlignCenter)
        self.l_processing.setObjectName("l_processing")
        
    # LOGS AREA @@@@@@@@@@#################################  
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(550, 80, 211, 411))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.content_data = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.l_logs = QtWidgets.QLabel(self.centralwidget)
        self.l_logs.setGeometry(QtCore.QRect(640, 50, 47, 13))
        self.l_logs.setObjectName("l_logs")

        self.l_name = QtWidgets.QLabel(self.centralwidget)
        self.l_name.setGeometry(QtCore.QRect(700, 540, 47, 13))
        self.l_name.setTextFormat(QtCore.Qt.AutoText)
        self.l_name.setObjectName("l_name")

    # ENERGY METER LABEL FIED ##############
        self.em_aa = QtWidgets.QLabel(self.centralwidget)
        self.em_aa.setGeometry(QtCore.QRect(30, 110, 91, 20))
        self.em_aa.setObjectName("em_aa")
        self.em_bb = QtWidgets.QLabel(self.centralwidget)
        self.em_bb.setGeometry(QtCore.QRect(30, 140, 91, 20))
        self.em_bb.setObjectName("em_bb")
        self.em_cc = QtWidgets.QLabel(self.centralwidget)
        self.em_cc.setGeometry(QtCore.QRect(30, 170, 91, 20))
        self.em_cc.setObjectName("em_cc")
        self.c_snoo = QtWidgets.QLabel(self.centralwidget)
        self.c_snoo.setGeometry(QtCore.QRect(30, 80, 141, 20))
        self.c_snoo.setObjectName("c_snoo")

    # ENERGU METER VALUE FIELD     ##########
        self.em_a = QtWidgets.QLineEdit(self.centralwidget)
        self.em_a.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.em_a.setPlaceholderText("Enter GUN A meter no")
        self.em_a.setObjectName("em_a")
        self.em_b = QtWidgets.QLineEdit(self.centralwidget)
        self.em_b.setGeometry(QtCore.QRect(180, 140, 113, 20))
        self.em_b.setPlaceholderText("Enter GUN B meter no")
        self.em_b.setObjectName("em_b")
        self.em_c = QtWidgets.QLineEdit(self.centralwidget)
        self.em_c.setGeometry(QtCore.QRect(180, 170, 113, 20))
        self.em_c.setPlaceholderText("Enter GUN c meter no")
        self.em_c.setObjectName("em_c")
        self.c_sno = QtWidgets.QLineEdit(self.centralwidget)
        self.c_sno.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.c_sno.setText("")
        self.c_sno.setObjectName("c_sno")

    # ENGINEER NAME ********************    
        self.fengg = QtWidgets.QFrame(self.centralwidget)
        self.fengg.setGeometry(QtCore.QRect(400, 79, 120, 141))
        self.fengg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fengg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fengg.setObjectName("fengg")

        self.l_engineer = QtWidgets.QLabel(self.fengg) # LABEL for text rngg name 
        self.l_engineer.setGeometry(QtCore.QRect(0, 0, 101, 20))
        self.l_engineer.setObjectName("l_engineer")

        self.eb_japesh = QtWidgets.QRadioButton(self.fengg) # japesh *****
        self.eb_japesh.setGeometry(QtCore.QRect(0, 90, 82, 17))
        self.eb_japesh.setObjectName("eb_japesh")

        self.eb_pradeep = QtWidgets.QRadioButton(self.fengg) # pradeep ****
        self.eb_pradeep.setGeometry(QtCore.QRect(0, 30, 82, 17))
        self.eb_pradeep.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.eb_pradeep.setChecked(True)
        self.eb_pradeep.setObjectName("eb_pradeep")

        self.eb_sahu = QtWidgets.QRadioButton(self.fengg) # Akhil ***
        self.eb_sahu.setGeometry(QtCore.QRect(0, 120, 82, 17))
        self.eb_sahu.setObjectName("eb_sahu")

        self.eb_anshul = QtWidgets.QRadioButton(self.fengg) # anshul
        self.eb_anshul.setGeometry(QtCore.QRect(0, 60, 82, 17))
        self.eb_anshul.setObjectName("eb_anshul")

        self.fengg_l = QtWidgets.QLabel(self.centralwidget)
        self.fengg_l.setGeometry(QtCore.QRect(30, 200, 261, 31))
        self.fengg_l.setObjectName("fengg_l")

    # gun 1 selection column **********************    
        self.fGUN1 = QtWidgets.QFrame(self.centralwidget)
        self.fGUN1.setGeometry(QtCore.QRect(30, 270, 141, 121))
        self.fGUN1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fGUN1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fGUN1.setObjectName("fGUN1")

        self.gb_ccs = QtWidgets.QRadioButton(self.fGUN1) # ccs button 
        self.gb_ccs.setGeometry(QtCore.QRect(0, 40, 82, 17))
        self.gb_ccs.setObjectName("gb_ccs")

        self.gb_gbt = QtWidgets.QRadioButton(self.fGUN1) # gbt button
        self.gb_gbt.setGeometry(QtCore.QRect(0, 70, 82, 17))
        self.gb_gbt.setObjectName("gb_gbt")

        self.gb_chademo = QtWidgets.QRadioButton(self.fGUN1)# chademo button
        self.gb_chademo.setGeometry(QtCore.QRect(0, 100, 82, 17))
        self.gb_chademo.setObjectName("gb_chademo") 

        self.s_gun1 = QtWidgets.QLabel(self.fGUN1) # select text label
        self.s_gun1.setGeometry(QtCore.QRect(0, 10, 81, 16))
        self.s_gun1.setObjectName("s_gun1")
    
    #gun 2 selection *******************************************
        self.fGUN2 = QtWidgets.QWidget(self.centralwidget)
        self.fGUN2.setGeometry(QtCore.QRect(200, 270, 141, 121))
        self.fGUN2.setObjectName("fGUN2")

        self.gb_ccs_2 = QtWidgets.QRadioButton(self.fGUN2) # ccs 2
        self.gb_ccs_2.setGeometry(QtCore.QRect(0, 40, 82, 17))
        self.gb_ccs_2.setObjectName("gb_ccs_2")

        self.gb_gbt_2 = QtWidgets.QRadioButton(self.fGUN2) # gbt 2
        self.gb_gbt_2.setGeometry(QtCore.QRect(0, 70, 82, 17))
        self.gb_gbt_2.setObjectName("gb_gbt_2")

        self.gb_chademo_2 = QtWidgets.QRadioButton(self.fGUN2) #chademo 2
        self.gb_chademo_2.setGeometry(QtCore.QRect(0, 100, 82, 17))
        self.gb_chademo_2.setObjectName("gb_chademo_2")

        self.s_gun2 = QtWidgets.QLabel(self.fGUN2) # select gun 2 text 
        self.s_gun2.setGeometry(QtCore.QRect(0, 10, 81, 16))
        self.s_gun2.setObjectName("s_gun2")

    # GUN 3 selection column ***************************
        self.fGUN3 = QtWidgets.QFrame(self.centralwidget)
        self.fGUN3.setGeometry(QtCore.QRect(400, 270, 131, 91))
        self.fGUN3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fGUN3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fGUN3.setObjectName("fGUN3")

        self.gb_type2 = QtWidgets.QRadioButton(self.fGUN3) # type 2
        self.gb_type2.setGeometry(QtCore.QRect(0, 40, 82, 17))
        self.gb_type2.setObjectName("gb_type2")

        self.gb_na = QtWidgets.QRadioButton(self.fGUN3) # na
        self.gb_na.setGeometry(QtCore.QRect(0, 70, 82, 17))
        self.gb_na.setObjectName("gb_na")

        self.s_gun3 = QtWidgets.QLabel(self.fGUN3) # select gun 3 text 
        self.s_gun3.setGeometry(QtCore.QRect(0, 10, 91, 16))
        self.s_gun3.setObjectName("s_gun3")

    # gun status
        self.s_gun1status = QtWidgets.QLabel(self.centralwidget)
        self.s_gun1status.setGeometry(QtCore.QRect(30, 400, 141, 16))
        self.s_gun1status.setObjectName("s_gun1status") #gun1 status
        self.s_gun2status = QtWidgets.QLabel(self.centralwidget)
        self.s_gun2status.setGeometry(QtCore.QRect(200, 400, 141, 16))
        self.s_gun2status.setObjectName("s_gun1status_2") #gun 2 status
        self.s_gun3status = QtWidgets.QLabel(self.centralwidget)
        self.s_gun3status.setGeometry(QtCore.QRect(400, 380, 141, 16))
        self.s_gun3status.setObjectName("s_gun1status_3")  #gun 3 status

        self.b_submit = QtWidgets.QPushButton(self.centralwidget) # submit btn 
        self.b_submit.setGeometry(QtCore.QRect(400, 30, 101, 31))
        self.b_submit.setObjectName("b_submit")

        self.script_btn = QtWidgets.QPushButton(self.centralwidget)
        self.script_btn.setGeometry(QtCore.QRect(30, 30, 101, 31))
        self.script_btn.setObjectName("script_btn")

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(550, 510, 101, 31))
        self.reset_btn.setObjectName("reset_btn")
    #**********************************************************************
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.l_logs.setText(_translate("MainWindow", "LOGS"))

        self.l_processing.setText(_translate("MainWindow", "PROCESSING"))

        self.c_snoo.setText(_translate("MainWindow", "CHARGER SERIAL NUMBER"))
        self.em_aa.setText(_translate("MainWindow", "GUN A EM S.No"))
        self.em_bb.setText(_translate("MainWindow", "GUN B EM S.No"))
        self.em_cc.setText(_translate("MainWindow", "GUN C EM S.No"))

        self.em_b.setDisabled(True)
        self.em_b.setDisabled(True)
        self.em_a.textChanged.connect(self.ema_val)
        self.em_b.textChanged.connect(self.emb_val)

        self.s_gun1.setText(_translate("MainWindow", "SELECT GUN 1"))
        self.gb_ccs.setText(_translate("MainWindow", "CCS"))
        self.gb_ccs.clicked.connect(self.gun1_on_click)
        self.gb_gbt.setText(_translate("MainWindow", "GB/T"))
        self.gb_gbt.toggled.connect(self.gun1_on_click)
        self.gb_chademo.setText(_translate("MainWindow", "Chademo"))
        self.gb_chademo.toggled.connect(self.gun1_on_click)

        self.s_gun2.setText(_translate("MainWindow", "SELECT GUN 2"))
        self.gb_ccs_2.setText(_translate("MainWindow", "CCS"))
        self.gb_ccs_2.toggled.connect(self.gun2_on_click)
        self.gb_gbt_2.setText(_translate("MainWindow", "GB/T"))
        self.gb_gbt_2.toggled.connect(self.gun2_on_click)
        self.gb_chademo_2.setText(_translate("MainWindow", "Chademo"))
        self.gb_chademo_2.toggled.connect(self.gun2_on_click)

        self.s_gun3.setText(_translate("MainWindow", "SELECT GUN 3"))
        self.gb_type2.setText(_translate("MainWindow", "Type 2"))
        self.gb_type2.toggled.connect(self.gun3_on_click)
        self.gb_na.setText(_translate("MainWindow", "NA"))
        self.gb_na.toggled.connect(self.gun3_on_click)

        self.s_gun1status.setText(_translate("MainWindow", "Nothing Selected"))
        self.s_gun2status.setText(_translate("MainWindow", "Nothing Selected"))
        self.s_gun3status.setText(_translate("MainWindow", "Nothing Selected"))


        self.l_engineer.setText(_translate("MainWindow", "TESTING ENGINEER"))
        self.eb_japesh.setText(_translate("MainWindow", "JAPESH"))
        self.eb_japesh.toggled.connect(self.engg_click)
        self.eb_pradeep.setText(_translate("MainWindow", "PRADEEP"))
        self.eb_pradeep.toggled.connect(self.engg_click)
        self.eb_sahu.setText(_translate("MainWindow", "AKHIL"))
        self.eb_sahu.toggled.connect(self.engg_click)
        self.eb_anshul.setText(_translate("MainWindow", "ANSHUL"))
        self.eb_anshul.toggled.connect(self.engg_click)

        self.fengg_l.setText(_translate("MainWindow", "NOTHING SELECTED"))

        self.l_name.setText(_translate("MainWindow", "by ANSHUL"))
    
        self.b_submit.setText(_translate("MainWindow", "GENERATE"))
        self.b_submit.clicked.connect(self.start_generate)

        self.script_btn.setText(_translate("MainWindow", "START"))
        self.script_btn.clicked.connect(self.start_uart)

        self.reset_btn.setText(_translate("MainWindow", "RESET"))
        self.reset_btn.clicked.connect(self.reset)

# functions ##############################################

    def ema_val(self, text):
        em_length = 12
        if len(text) == em_length:
            meter_a = text
            textt = QtWidgets.QLabel(f"GUN A EM S.No is {meter_a}")
            self.content_data.addWidget(textt)
            context["a_dcem"] = meter_a
            print(meter_a)
            self.em_b.setDisabled(False)
            self.em_b.setFocus()
            self.em_a.setDisabled(True)

    def emb_val(self, text):
        em_length = 12
        if len(text) == em_length:
            meter_b = text
            textt = QtWidgets.QLabel(f"GUN B EM S.No is {meter_b}")
            self.content_data.addWidget(textt)
            context["b_dcem"] = meter_b
            print(meter_b)
            self.em_b.setDisabled(True)
        # popup for emc
            gun_c_msg = QtWidgets.QMessageBox()
            gun_c_msg.setWindowTitle("conformation for GUN C")
            gun_c_msg.setText("GUN C is avaliable or not")
            gun_c_msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            clicked_button = gun_c_msg.exec_()

            if clicked_button == QtWidgets.QMessageBox.Yes:
                self.em_c.textChanged.connect(self.emc_val)
                self.em_c.setDisabled(False)
                self.em_c.setFocus()
            if clicked_button == QtWidgets.QMessageBox.No:
                self.em_c.setText("NA")
                context["c_dcem"] = "NA"
                context["c_current"] = "NA"
                context["c_voltage"] = "NA"

                textt = QtWidgets.QLabel("GUN C isn't AVALIABLE ")
                self.content_data.addWidget(textt)
                self.gb_na.setChecked(True)
                self.em_c.setDisabled(True)

    def emc_val(self, text):
        em_length = 12
        if len(text) == em_length:
            meter_c = text
            textt = QtWidgets.QLabel(f"GUN  EM S.No is {meter_c}")
            self.content_data.addWidget(textt)
            context["c_dcem"] = meter_c
            print(meter_c)
            self.em_b.setDisabled(True)
            self.em_c.setDisabled(True)

    def gun1_on_click(self):

        if self.gb_ccs.isChecked():
            x = "gun 1 is ccs"
            print(x)
            context["a_gun"] = "CCS"
            # values.append(x)
            self.s_gun1status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_gbt.setDisabled(True)
            self.gb_chademo.setDisabled(True)

        if self.gb_gbt.isChecked():
            x = "gun 1 is gbt"
            print(x)
            context["a_gun"] = "GB/T"
            # values.append(x)
            self.s_gun1status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_ccs.setDisabled(True)
            self.gb_chademo.setDisabled(True)

        if self.gb_chademo.isChecked():
            x = "gun 1 is chademo"
            print(x)
            context["a_gun"] = "CHADEMO"
            # values.append(x)
            self.s_gun1status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_gbt.setDisabled(True)
            self.gb_ccs.setDisabled(True)
    
    def gun2_on_click(self):

        if self.gb_ccs_2.isChecked():
            x = "gun 2 is ccs"
            print(x)
            context["b_gun"] = "CCS"
            # values.append(x)
            self.s_gun2status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_gbt_2.setDisabled(True)
            self.gb_chademo_2.setDisabled(True)

        if self.gb_gbt_2.isChecked():
            x = "gun 2 is gbt"
            print(x)
            context["b_gun"] = "GB/T"
            # values.append(x)
            self.s_gun2status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_chademo_2.setDisabled(True)
            self.gb_ccs_2.setDisabled(True)

        if self.gb_chademo_2.isChecked():
            x = "gun 2 is chademo"
            print(x)
            context["b_gun"] = "CHADEMO"
            # values.append(x)
            self.s_gun2status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_gbt_2.setDisabled(True)
            self.gb_ccs_2.setDisabled(True)

    def gun3_on_click(self):
        if self.gb_type2.isChecked():
            x = "gun 3 is Type 2"
            print(x)
            context["c_gun"] = "TYPE-2"
            # values.append(x)
            self.s_gun3status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_na.setDisabled(True)

        if self.gb_na.isChecked():
            x = "gun 3 is na"
            print(x)
            context["c_gun"] = "NA"
            # values.append(x)
            self.s_gun3status.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.gb_type2.setDisabled(True)
    
    def engg_click(self):
        if self.eb_japesh.isChecked():
            x = "TESTING ENGINEER IS JAPESH "
            print(x)
            # values.append(x)
            self.fengg_l.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.eb_anshul.setDisabled(True)
            self.eb_pradeep.setDisabled(True)
            self.eb_sahu.setDisabled(True)
            context["t_engg"] = "JAPESH"

        if self.eb_pradeep.isChecked():
            x = "TESTING ENGINEER IS PRADEEP "
            print(x)
            # values.append(x)
            self.fengg_l.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.eb_anshul.setDisabled(True)
            self.eb_japesh.setDisabled(True)
            self.eb_sahu.setDisabled(True)
            context["t_engg"] = "PRADEEP"

        if self.eb_sahu.isChecked():
            x = "TESTING ENGINEER IS AKHIL "
            print(x)
            # values.append(x)
            self.fengg_l.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.eb_anshul.setDisabled(True)
            self.eb_pradeep.setDisabled(True)
            self.eb_japesh.setDisabled(True)
            context["t_engg"] = "AKHILESHWAR"

        if self.eb_anshul.isChecked():
            x = "TESTING ENGINEER IS ANSHUL "
            print(x)
            # values.append(x)
            self.fengg_l.setText(x)
            textt = QtWidgets.QLabel(x)
            self.content_data.addWidget(textt)
            self.eb_japesh.setDisabled(True)
            self.eb_pradeep.setDisabled(True)
            self.eb_sahu.setDisabled(True)
            context["t_engg"] = "ANSHUL"
    
    def start_generate(self): # data used by generate fun 

        self.value_worker = ValueThread()
        self.value_worker.execute()

    #     template_path = "tempate.docx"
    #     data_csv_path = "data.csv"
    #     output_docx_path = "g.docx"
    #     output_pdf_path = "p.pdf"
    #     input_file = 'data.csv'  
    #     output_file = 'output.csv' 
    #     import_context = context

    #     self.generate_worker = GenerateThread(template_path, data_csv_path, output_docx_path, output_pdf_path, input_file, output_file, import_context) #thread for generate thing py file
    #     self.generate_worker.result_signal.connect(self.generate_data)
    #     self.generate_worker.start()

    # def generate_data(self, message):
    #     x = message
    #     textt = QtWidgets.QLabel(x)
    #     self.content_data.addWidget(textt)
   

    def start_uart(self):
        port='COM9'
        baudrate=115200
        data_csv_path="data.csv" # file path for csv created by script btn
        self.uart_worker = UartThread(port, baudrate, data_csv_path)
        self.uart_worker.chargerSn.connect(self.uart_data)
        self.uart_worker.execute()

    def uart_data(self, message):
        if "chargePointSerialNumber" and "chargePointModel" in message:
            print(message)
            x = message["chargePointSerialNumber"]
            y = message["chargePointModel"]
            z = (f"ChargerSno: \n {y}#{x}")
            textt = QtWidgets.QLabel(z)
            self.content_data.addWidget(textt)
            self.c_sno.setText(z)
            self.c_sno.setDisabled(True)
            self.em_a.setFocus()

    def reset(self):
        while self.content_data.count():
            item = self.content_data.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.em_a.clear()
        self.em_b.clear()
        self.em_c.clear()
        self.c_sno.clear()
        self.em_a.setDisabled(False)
        self.em_b.setDisabled(False)
        self.em_c.setDisabled(False)
        self.c_sno.setDisabled(False)

        self.eb_japesh.setAutoExclusive(False)
        self.eb_pradeep.setAutoExclusive(False)
        self.eb_sahu.setAutoExclusive(False)
        self.eb_anshul.setAutoExclusive(False)
        self.eb_japesh.setChecked(False)
        self.eb_pradeep.setChecked(False)
        self.eb_sahu.setChecked(False)
        self.eb_anshul.setChecked(False)
        self.eb_japesh.setDisabled(False)
        self.eb_pradeep.setDisabled(False)
        self.eb_sahu.setDisabled(False)
        self.eb_anshul.setDisabled(False)
        self.fengg_l.setText("NOTHING SELECTED")
        
        self.gb_ccs.setAutoExclusive(False)
        self.gb_gbt.setAutoExclusive(False)
        self.gb_chademo.setAutoExclusive(False)
        self.gb_ccs.setChecked(False)
        self.gb_gbt.setChecked(False)
        self.gb_chademo.setChecked(False)
        self.gb_ccs.setChecked(False)
        self.gb_gbt.setChecked(False)
        self.gb_chademo.setChecked(False)
        self.s_gun1status.setText("NOTHING SELECTED")
        self.gb_ccs_2.setAutoExclusive(False)
        self.gb_gbt_2.setAutoExclusive(False)
        self.gb_chademo_2.setAutoExclusive(False)
        self.gb_ccs_2.setChecked(False)
        self.gb_gbt_2.setChecked(False)
        self.gb_chademo_2.setChecked(False)
        self.gb_ccs_2.setDisabled(False)
        self.gb_gbt_2.setDisabled(False)
        self.gb_chademo_2.setDisabled(False)
        self.s_gun2status.setText("NOTHING SELECTED")
        self.gb_type2.setAutoExclusive(False)
        self.gb_na.setAutoExclusive(False)
        self.gb_type2.setChecked(False)
        self.gb_na.setChecked(False)
        self.gb_type2.setDisabled(False)
        self.gb_na.setDisabled(False)
        self.s_gun3status.setText("NOTHING SELECTED")

        temp_files = ['data.csv', 'output.csv'] 
        for file in temp_files:
            if os.path.exists(file):
                try:
                    os.remove(file)
                    print(f"Deleted {file}")
                except Exception as e:
                    print(f"Error deleting {file}: {e}")

        QtWidgets.QMessageBox.information(self, "Reset", "All fields have been reset and temporary files deleted.")       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Ui_MainWindow.text_logs()
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FSave.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import subprocess 
import os
from os import path
import shutil
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from datetime import *
import time


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def  __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        def autosave():
            a = True
            g = 0
            while (a == True):
                process = subprocess.Popen('pgrep ' + 'Microsoft Word', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                my_pid, err = process.communicate()
                b = str(my_pid)
                l = len(b)
                integ = []
                i = 0
                while i < l:
                    s_int = ''
                    a = b[i]
                    while '0' <= a <= '9':
                        s_int += a
                        i += 1
                        if i < l:
                            a = b[i]
                        else:
                            break
                    i += 1
                    if s_int != '':
                        integ.append(int(s_int))
                t = 0
                for k in integ:
                    t += 1
                print(t)
                if t == 1:
                    g += 1
                if t == 1:
                    progress = True
                elif t == 0:
                    progress = False
            
                if progress == True:
                    keyboard.send('cmd + s')
                    print('Autosave')
                    time.sleep(60)
                time.sleep(5)
                a = True
                if g != 0 and t == 0:
                    a = False
            while (a == True):
                process = subprocess.Popen('pgrep ' + 'Microsoft Excel', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                my_pid, err = process.communicate()
                b = str(my_pid)
                l = len(b)
                integ = []
                i = 0
                while i < l:
                    s_int = ''
                    a = b[i]
                    while '0' <= a <= '9':
                        s_int += a
                        i += 1
                        if i < l:
                            a = b[i]
                        else:
                            break
                    i += 1
                    if s_int != '':
                        integ.append(int(s_int))
                t = 0
                for k in integ:
                    t += 1
                print(t)
                if t == 1:
                    g += 1
                if t == 1:
                    progressx = True
                elif t == 0:
                    progressx = False
            
                if progressx == True:
                    keyboard.send('cmd + s')
                    print('Autosave')
                    time.sleep(60)
                time.sleep(60)
                a = True
                if g != 0 and t == 0:
                    a = False
            while (a == True):
                process = subprocess.Popen('pgrep ' + 'Adobe Photoshop', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                my_pid, err = process.communicate()
                b = str(my_pid)
                l = len(b)
                integ = []
                i = 0
                while i < l:
                    s_int = ''
                    a = b[i]
                    while '0' <= a <= '9':
                        s_int += a
                        i += 1
                        if i < l:
                            a = b[i]
                        else:
                            break
                    i += 1
                    if s_int != '':
                        integ.append(int(s_int))
                t = 0
                for k in integ:
                    t += 1
                print(t)
                if t == 1:
                    g += 1
                if t == 1:
                    progress = True
                elif t == 0:
                    progress = False
            
                if progress == True:
                    keyboard.send('cmd + s')
                    print('Autosave')
                    time.sleep(60)
                time.sleep(5)
                a = True
                if g != 0 and t == 0:
                    a = False
            while (a == True):
                process = subprocess.Popen('pgrep ' + 'FL Studio', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                my_pid, err = process.communicate()
                b = str(my_pid)
                print(b)
                l = len(b)
                integ = []
                i = 0
                while i < l:
                    s_int = ''
                    a = b[i]
                    while '0' <= a <= '9':
                        s_int += a
                        i += 1
                        if i < l:
                            a = b[i]
                        else:
                            break
                    i += 1
                    if s_int != '':
                        integ.append(int(s_int))
                t = 0
                for k in integ:
                    t += 1
                print(t)
                if t == 1:
                    g += 1
                if t == 1:
                    progress = True
                elif t == 0:
                    progress = False
            
                if progress == True:
                    keyboard.send('cmd + s')
                    print('Autosave')
                    time.sleep(60)
                time.sleep(5)
                a = True
                if g != 0 and t == 0:
                    a = False
            while (a == True):
                process = subprocess.Popen('pgrep ' + 'Vegas Pro', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                my_pid, err = process.communicate()
                b = str(my_pid)
                l = len(b)
                integ = []
                i = 0
                while i < l:
                    s_int = ''
                    a = b[i]
                    while '0' <= a <= '9':
                        s_int += a
                        i += 1
                        if i < l:
                            a = b[i]
                        else:
                            break
                    i += 1
                    if s_int != '':
                        integ.append(int(s_int))
                t = 0
                for k in integ:
                    t += 1
                print(t)
                if t == 1:
                    g += 1
                if t == 1:
                    progress = True
                elif t == 0:
                    progress = False
            
                if progress == True:
                    keyboard.send('cmd + s')
                    print('Autosave')
                    time.sleep(60)
                time.sleep(5)
                a = True
                if g != 0 and t == 0:
                    a = False
        autosave()
class Ui_MainWindow(QMainWindow):
    mysignal = QtCore.pyqtSignal(str)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 600, 40))
        self.groupBox.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 0, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border: 0;\n"
"background-color: rgba(127, 255, 212, 0);\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 0, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border: 0;\n"
"background-color: rgba(127, 255, 212, 0);\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 16px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(15, 10, 108, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(127, 255, 212, 0);\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 7, 250, 25))
        self.label_2.setStyleSheet("border: 0;\n"
"border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 0.83);\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(69, 80, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 80, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(449, 80, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(69, 210, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 210, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgba(127, 255, 230, 1);\n"
"border: 1px solid #000000;\n"
"border-radius: 5px;\n"
"font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(68, 150, 101, 21))
        self.label_3.setStyleSheet("font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(281, 150, 51, 21))
        self.label_4.setStyleSheet("font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(476, 150, 41, 21))
        self.label_5.setStyleSheet("font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(88, 280, 51, 21))
        self.label_6.setStyleSheet("font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(266, 280, 81, 21))
        self.label_7.setStyleSheet("font-family: Ubuntu;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;")
        self.label_7.setObjectName("label_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(556, 340, 30, 30))
        self.pushButton_9.setStyleSheet("font-family: Ubuntu;\n"
"color: rgb(255, 255, 255);\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"border-radius: 15px;\n"
"background-color: rgba(127, 255, 230, 1);")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_function()
        self.mythread = MyThread()
        self.pushButton_2.clicked.connect(self.on_clicked)
    def on_clicked(self):
        self.mythread.start()  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ForSave"))
        self.pushButton_2.setText(_translate("MainWindow", "Запуск"))
        self.pushButton_3.setText(_translate("MainWindow", "Перенос"))
        self.label.setText(_translate("MainWindow", "Путь к файлу:"))
        self.pushButton_4.setText(_translate("MainWindow", "PS"))
        self.pushButton_5.setText(_translate("MainWindow", "W"))
        self.pushButton_6.setText(_translate("MainWindow", "EX"))
        self.pushButton_7.setText(_translate("MainWindow", "V"))
        self.pushButton_8.setText(_translate("MainWindow", "FL"))
        self.label_3.setText(_translate("MainWindow", "Photoshop"))
        self.label_4.setText(_translate("MainWindow", "Word"))
        self.label_5.setText(_translate("MainWindow", "Excel"))
        self.label_6.setText(_translate("MainWindow", "Vegas"))
        self.label_7.setText(_translate("MainWindow", "FL Studio"))
        self.pushButton_9.setText(_translate("MainWindow", "?"))
        self.label_2.setText(os.getcwd())
        self.make_dirs('FMicrosoft Word')
        self.make_dirs('FMicrosoft Excel')
        self.make_dirs('FPhotoshop')
        self.make_dirs('FVegas')
        self.make_dirs('FFl Studio')  

    def add_function(self):
        
        self.pushButton_3.clicked.connect(lambda: self.replace())
        self.pushButton_5.clicked.connect(lambda: self.opened('FMicrosoft Word'))
        self.pushButton_6.clicked.connect(lambda: self.opened('FMicrosoft Excel'))
        self.pushButton_7.clicked.connect(lambda: self.opened('FVegas'))
        self.pushButton_8.clicked.connect(lambda: self.opened('FFl Studio'))
        self.pushButton_4.clicked.connect(lambda: self.opened('FPhotoshop'))
        self.pushButton_9.clicked.connect(lambda: self.about())


    def about(self):
        ab = QMessageBox()
        ab.setWindowTitle('About')
        ab.setText('Подсказка по пользованию <hr> Кнопка "Запуск" включает программу автосохранения. <br> Функция автосохранения включается, когда работает хотя бы одна из предложенных программ: Photoshop, Microsoft Word, Microsoft Excel, Vegas, FL Studio. Функция выключается, когда пользователь завершает работу в программе и закрывает её. <hr> Кнопка "Перенос" переносит все файлы из выбранной области в соответствующие папки, созданные программой. К этим папкам осуществляется доступ через кнопки с соответсвующими названиями в программе. <hr> В верхней части указан путь к папке, в которой находится программа и папки с перенесёнными файлами. <hr> Чтобы узнать подробности, читайте файл ReadMe в архиве программы или на сайте. <hr> Разработка: Нестеров Денис, Мартыненко Роман, Трутнев Григорий.')
        ab.exec_()
       
    
    def opened (self, programm):
        path = str(os.getcwd()) + '/' + programm
        if os.path.exists(path):
            subprocess.call(["open", path])

    def make_dirs(self, folder):
        if not os.path.isdir(folder):
            os.mkdir(folder)

    def replace(self):
        a = []                                                
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        a.append(dirlist)
        for q in a:
            if q != 0:
                oldplace = q
        docxs = []
        xls = []
        ps = []
        vp = []
        fl = []
        old = []
        old_xls = []
        old_ps = []
        old_vp =[]
        old_fl =[]
        name = []
        name_xls = []
        name_ps = []
        name_vp = []
        name_fl = []
        rec = []
        rec_xls = []
        rec_ps = []
        rec_vp = []
        rec_fl =[]
        for root, dirs, files in os.walk(oldplace):
            for file in files:
                if file.endswith('docx') and not file.startswith('~'):
                    a = str(root + file)
                    if not a.count("FMicrosoft Word"):
                        docxs.append(os.path.join(root, file))
                    else:
                        old.append(os.path.join(file))
        for root, dirs, files in os.walk(oldplace):
            for file in files:
                if file.endswith('xlsx') and not file.startswith('~'):
                    a = str(root + file)
                    if not a.count("FMicrosoft Excel"):
                        xls.append(os.path.join(root, file))
                    else:
                        old_xls.append(os.path.join(file))
        for root, dirs, files in os.walk(oldplace):
            for file in files:
                if file.endswith('psd') and not file.startswith('~'):
                    a = str(root + file)
                    if not a.count("FPhotoshop"):
                        ps.append(os.path.join(root, file))
                    else:
                        old_ps.append(os.path.join(file))
        for root, dirs, files in os.walk(oldplace):
            for file in files:
                if file.endswith('veg') and not file.startswith('~'):
                    a = str(root + file)
                    if not a.count("FVegas"):
                        vp.append(os.path.join(root, file))
                    else:
                        old_vp.append(os.path.join(file))
        for root, dirs, files in os.walk(oldplace):
            for file in files:
                if file.endswith('flp') and not file.startswith('~'):
                    a = str(root + file)
                    if not a.count("FFl Studio"):
                        fl.append(os.path.join(root, file))
                    else:
                        old_fl.append(os.path.join(file))
        for i in docxs:
            for f in old:
                together = str(i)
                d = str(f)
                if together.count(d):
                    print('Такой файл есть')
                    name.append(i)
                    rec.append(f)           
        r = list(set(docxs) - set(name))
        for h in r:
            if path.exists(h):
                shutil.move(h, "FMicrosoft Word")
                print('+' + 'docx')
        for v in name:
            for z in rec:
                q = str(z)
                os.rename(v, 'Другой ' + q)
            shutil.move('Другой ' + q, "FMicrosoft Word")
            print('+' + 'docx')
        for i in xls:
            for f in old_xls:
                together = str(i)
                d = str(f)
                if together.count(d):
                    print('Такой файл есть')
                    name_xls.append(i)
                    rec_xls.append(f)           
        r = list(set(xls) - set(name_xls))
        for h in r:
            if path.exists(h):
                shutil.move(h, "FMicrosoft Excel")
                print('+' + 'xlsx')
        for v in name_xls:
            for z in rec_xls:
                q = str(z)
                os.rename(v, 'Другой ' + q)
            shutil.move('Другой ' + q, "FMicrosoft Excel")
            print('+' + 'xlsx')
        for i in ps:
            for f in old_ps:
                together = str(i)
                d = str(f)
                if together.count(d):
                    print('Такой файл есть')
                    name_ps.append(i)
                    rec_ps.append(f)           
        r = list(set(ps) - set(name_ps))
        for h in r:
            if path.exists(h):
                shutil.move(h, "FPhotoshop")
                print('+' + 'psd')
        for v in name_ps:
            for z in rec_ps:
                q = str(z)
                os.rename(v, 'Другой ' + q)
            shutil.move('Другой ' + q, "FPhotoshop")
            print('+' + 'psd')   
        for i in vp:
            for f in old_vp:
                together = str(i)
                d = str(f)
                if together.count(d):
                    print('Такой файл есть')
                    name_vp.append(i)
                    rec_vp.append(f)           
        r = list(set(vp) - set(name_vp))
        for h in r:
            if path.exists(h):
                shutil.move(h, "FVegas")
                print('+' + 'veg')
        for v in name_vp:
            for z in rec_vp:
                q = str(z)
                os.rename(v, 'Другой ' + q)
            shutil.move('Другой ' + q, "FVegas")
            print('+' + 'veg')
        for i in fl:
            for f in old_fl:
                together = str(i)
                d = str(f)
                if together.count(d):
                    print('Такой файл есть')
                    name_fl.append(i)
                    rec_fl.append(f)           
        r = list(set(fl) - set(name_fl))
        for h in r:
            if path.exists(h):
                shutil.move(h, "FFl Studio")
                print('+' + 'flp')
        for v in name_fl:
            for z in rec_fl:
                q = str(z)
                os.rename(v, 'Другой ' + q)
            shutil.move('Другой ' + q, "FFl Studio")
            print('+' + 'flp')
                    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

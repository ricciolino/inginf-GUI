from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QAction, QMessageBox,
                             QLineEdit, QLabel, QTabWidget)

import subprocess
import sys
import os
from pathlib import Path

def get_screen_res():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()
    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]
    resolution = resolution.decode("utf-8")
    width, height = resolution.split('x')
    return width,height

SCREEN_WIDTH,SCREEN_HEIGHT = get_screen_res()

WINDOW_WIDTH = 516
WINDOW_HEIGHT = 526
WINDOW_XPOS = (int(SCREEN_WIDTH)-WINDOW_WIDTH)/2
WINDOW_YPOS = (int(SCREEN_HEIGHT)-WINDOW_HEIGHT)/2

class Window(QWidget):
    def __init__(self,filevoti,filevotifin):
        super().__init__()

        self.votiPath = filevoti
        self.votifinPath = filevotifin
       
        # main vertical layout
        self.vLayout = QVBoxLayout()
        self.setLayout(self.vLayout)

        # 3 main horizontal layout
        self.hLayout1 = QHBoxLayout()
        self.hLayout4 = QHBoxLayout()
        self.hLayout2 = QHBoxLayout()
        self.hLayout3 = QHBoxLayout()

        # tabWidget in hLayout1
        self.tabWid = QTabWidget()
        f = self.tabWid.font()
        f.setPointSize(8)
        f.setBold(True)
        self.tabWid.setFont(f)
        # tab ATTUALE
        self.tabAttuale = QWidget()
        self.tabWid.addTab(self.tabAttuale,"ATTUALE")
        self.tabAttuale.layout = QGridLayout()
        self.corsoAttLabel = QLabel("CORSO")
        f = self.corsoAttLabel.font()
        f.setPointSize(8)
        self.corsoAttLabel.setFont(f)
        self.corsoAttLabel.setStyleSheet("background-color: yellow;")
        self.corsoAttLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.corsoAttLabel.setFixedHeight(30)
        self.cfuAttLabel = QLabel("CFU")
        f = self.cfuAttLabel.font()
        f.setPointSize(8)
        self.cfuAttLabel.setFont(f)
        self.cfuAttLabel.setStyleSheet("background-color: yellow;")
        self.cfuAttLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.votoAttLabel = QLabel("VOTO")
        f = self.votoAttLabel.font()
        f.setPointSize(8)
        self.votoAttLabel.setFont(f)
        self.votoAttLabel.setStyleSheet("background-color: yellow;")
        self.votoAttLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tabAttuale.layout.addWidget(self.corsoAttLabel,0,0)
        self.tabAttuale.layout.addWidget(self.cfuAttLabel,0,1)
        self.tabAttuale.layout.addWidget(self.votoAttLabel,0,2)
        self.tabAttuale.layout.setColumnStretch(0,10)
        self.tabAttuale.layout.setColumnStretch(1,1)
        self.tabAttuale.layout.setColumnStretch(2,1)
        self.matrix = self.MatrixFromFile(self.votiPath)
        for i in range(1,14):
            code = f'self.lineName_{i}_0 = QLineEdit(self.matrix[i-1][0])'
            exec(code)
            eval(f'self.lineName_{i}_0.setFont(f)')
            code = f'self.lineName_{i}_0.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineName_{i}_0.setAlignment(QtCore.Qt.AlignRight)'
            exec(code)
            code = f'self.lineName_{i}_0.editingFinished.connect(self.CheckForNumberOnLineName_{i}_0)'
            exec(code)
            code = f'self.lineName_{i}_0_firstValue = self.matrix[i-1][0]'
            exec(code)
            code = f'self.lineCfu_{i}_1 = QLineEdit(self.matrix[i-1][1])'
            exec(code)
            eval(f'self.lineCfu_{i}_1.setFont(f)')
            code = f'self.lineCfu_{i}_1.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineCfu_{i}_1.setAlignment(QtCore.Qt.AlignCenter)'
            exec(code)
            code = f'self.lineCfu_{i}_1.editingFinished.connect(self.CheckForNumberOnLineCfu_{i}_1)'
            exec(code)
            code = f'self.lineCfu_{i}_1_firstValue = self.matrix[i-1][1]'
            exec(code)
            code = f'self.lineVoto_{i}_2 = QLineEdit(self.matrix[i-1][2])'
            exec(code)
            eval(f'self.lineVoto_{i}_2.setFont(f)')
            code = f'self.lineVoto_{i}_2.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineVoto_{i}_2.setAlignment(QtCore.Qt.AlignCenter)'
            exec(code)
            code = f'self.lineVoto_{i}_2.editingFinished.connect(self.CheckForNumberOnLineVoto_{i}_2)'
            exec(code)
            code = f'self.lineVoto_{i}_2_firstValue = self.matrix[i-1][2]'
            exec(code)
            code = f'self.tabAttuale.layout.addWidget(self.lineName_{i}_0,i,0)'
            exec(code)
            code = f'self.tabAttuale.layout.addWidget(self.lineCfu_{i}_1,i,1)'
            exec(code)
            code = f'self.tabAttuale.layout.addWidget(self.lineVoto_{i}_2,i,2)'
            exec(code)
        self.tabAttuale.setLayout(self.tabAttuale.layout)
        # tab PREVISIONE
        self.tabPrevisione = QWidget()
        self.tabWid.addTab(self.tabPrevisione,"PREVISIONE")
        self.tabPrevisione.layout = QGridLayout()
        self.corsoPrevLabel = QLabel("CORSO")
        f = self.corsoPrevLabel.font()
        f.setPointSize(8)
        self.corsoPrevLabel.setFont(f)
        self.corsoPrevLabel.setStyleSheet("background-color: yellow;")
        self.corsoPrevLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.corsoPrevLabel.setFixedHeight(30)
        self.cfuPrevLabel = QLabel("CFU")
        f = self.cfuPrevLabel.font()
        f.setPointSize(8)
        self.cfuPrevLabel.setFont(f)
        self.cfuPrevLabel.setStyleSheet("background-color: yellow;")
        self.cfuPrevLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.votoPrevLabel = QLabel("VOTO")
        f = self.votoPrevLabel.font()
        f.setPointSize(8)
        self.votoPrevLabel.setFont(f)
        self.votoPrevLabel.setStyleSheet("background-color: yellow;")
        self.votoPrevLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tabPrevisione.layout.addWidget(self.corsoPrevLabel,0,0)
        self.tabPrevisione.layout.addWidget(self.cfuPrevLabel,0,1)
        self.tabPrevisione.layout.addWidget(self.votoPrevLabel,0,2)
        self.tabPrevisione.layout.setColumnStretch(0,10)
        self.tabPrevisione.layout.setColumnStretch(1,1)
        self.tabPrevisione.layout.setColumnStretch(2,1)
        self.matrix_fin = self.MatrixFromFile(self.votifinPath)
        for i in range(1,14):
            code = f'self.lineNameFin_{i}_0 = QLineEdit(self.matrix_fin[i-1][0])'
            exec(code)
            eval(f'self.lineNameFin_{i}_0.setFont(f)')
            code = f'self.lineNameFin_{i}_0.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineNameFin_{i}_0.setAlignment(QtCore.Qt.AlignRight)'
            exec(code)
            code = f'self.lineNameFin_{i}_0.editingFinished.connect(self.CheckForNumberOnLineNameFin_{i}_0)'
            exec(code)
            code = f'self.lineNameFin_{i}_0_firstValue = self.matrix_fin[i-1][0]'
            exec(code)
            code = f'self.lineCfuFin_{i}_1 = QLineEdit(self.matrix_fin[i-1][1])'
            exec(code)
            eval(f'self.lineCfuFin_{i}_1.setFont(f)')
            code = f'self.lineCfuFin_{i}_1.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineCfuFin_{i}_1.setAlignment(QtCore.Qt.AlignCenter)'
            exec(code)
            code = f'self.lineCfuFin_{i}_1.editingFinished.connect(self.CheckForNumberOnLineCfuFin_{i}_1)'
            exec(code)
            code = f'self.lineCfuFin_{i}_1_firstValue = self.matrix_fin[i-1][1]'
            exec(code)
            code = f'self.lineVotoFin_{i}_2 = QLineEdit(self.matrix_fin[i-1][2])'
            exec(code)
            eval(f'self.lineVotoFin_{i}_2.setFont(f)')
            code = f'self.lineVotoFin_{i}_2.setStyleSheet("background-color: lightgreen;")'
            exec(code)
            code = f'self.lineVotoFin_{i}_2.setAlignment(QtCore.Qt.AlignCenter)'
            exec(code)
            code = f'self.lineVotoFin_{i}_2.editingFinished.connect(self.CheckForNumberOnLineVotoFin_{i}_2)'
            exec(code)
            code = f'self.lineVotoFin_{i}_2_firstValue = self.matrix_fin[i-1][2]'
            exec(code)
            code = f'self.tabPrevisione.layout.addWidget(self.lineNameFin_{i}_0,i,0)'
            exec(code)
            code = f'self.tabPrevisione.layout.addWidget(self.lineCfuFin_{i}_1,i,1)'
            exec(code)
            code = f'self.tabPrevisione.layout.addWidget(self.lineVotoFin_{i}_2,i,2)'
            exec(code)
        self.tabPrevisione.setLayout(self.tabPrevisione.layout)
        # config and add tabWidget to horz layout
        self.tabWid.setStyleSheet("background-color: green;")
        self.tabWid.currentChanged.connect(self.TabChanged)
        self.hLayout1.addWidget(self.tabWid)

        # media aritmetica in hLayout2left e hLayout3left
        self.label_media_aritm = QLabel()
        self.label_media_aritm.setStyleSheet("background-color: yellow;")
        self.label_media_aritm.setText("MEDIA ARITMETICA")
        f = self.label_media_aritm.font()
        f.setPointSize(8)
        self.label_media_aritm.setFont(f)
        self.label_media_aritm.setAlignment(QtCore.Qt.AlignCenter)
        self.hLayout2left = QHBoxLayout()
        self.hLayout2left.addWidget(self.label_media_aritm)
        self.hLayout3left = QHBoxLayout()
        self.lineEdit_media_aritm = QLineEdit()
        f = self.lineEdit_media_aritm.font()
        f.setPointSize(8)
        self.lineEdit_media_aritm.setFont(f)
        self.lineEdit_media_aritm.setStyleSheet("background-color: lightgreen;")
        self.lineEdit_media_aritm.setFixedWidth(120)
        self.lineEdit_media_aritm.setAlignment(QtCore.Qt.AlignCenter)
        self.hLayout3left.addWidget(self.lineEdit_media_aritm)

        # media ponderata in hLayout2center e hLayout3center
        self.label_media_pond = QLabel()
        self.label_media_pond.setStyleSheet("background-color: yellow;")
        self.label_media_pond.setText("MEDIA PONDERATA")
        f = self.label_media_pond.font()
        f.setPointSize(8)
        self.label_media_pond.setFont(f)
        self.label_media_pond.setAlignment(QtCore.Qt.AlignCenter)
        self.hLayout2center = QHBoxLayout()
        self.hLayout2center.addWidget(self.label_media_pond)
        self.hLayout3center = QHBoxLayout()
        self.lineEdit_media_pond = QLineEdit()
        f = self.lineEdit_media_pond.font()
        f.setPointSize(8)
        self.lineEdit_media_pond.setFont(f)
        self.lineEdit_media_pond.setStyleSheet("background-color: lightgreen;")
        self.lineEdit_media_pond.setFixedWidth(120)
        self.lineEdit_media_pond.setAlignment(QtCore.Qt.AlignCenter)
        self.hLayout3center.addWidget(self.lineEdit_media_pond)

        # voto partenza laurea in hLayout2right e hLayout3right
        self.label_partenza_laurea = QLabel()
        self.label_partenza_laurea.setStyleSheet("background-color: yellow;")
        self.label_partenza_laurea.setText("VOTO PARTENZA LAUREA")
        f = self.label_partenza_laurea.font()
        f.setPointSize(8)
        self.label_partenza_laurea.setFont(f)
        self.label_partenza_laurea.setAlignment(QtCore.Qt.AlignCenter)
        self.hLayout2right = QHBoxLayout()
        self.hLayout2right.addWidget(self.label_partenza_laurea)
        self.hLayout3right = QHBoxLayout()
        self.lineEdit_partenza_laurea = QLineEdit()
        f = self.lineEdit_partenza_laurea.font()
        f.setPointSize(8)
        self.lineEdit_partenza_laurea.setFont(f)
        self.lineEdit_partenza_laurea.setStyleSheet("background-color: lightgreen;")
        self.lineEdit_partenza_laurea.setFixedWidth(120)
        self.lineEdit_partenza_laurea.setAlignment(QtCore.Qt.AlignCenter)
        #self.lineEdit_partenza_laurea.editingFinished.connect(self.PrintMatrix) #########
        self.hLayout3right.addWidget(self.lineEdit_partenza_laurea)

        # composizione hLayout2
        self.hLayout2.addLayout(self.hLayout2left)
        self.hLayout2.addLayout(self.hLayout2center)
        self.hLayout2.addLayout(self.hLayout2right)

        # composizione hLayout3
        self.hLayout3.addStretch(1)
        self.hLayout3.addLayout(self.hLayout3left)
        self.hLayout3.addStretch(2)
        self.hLayout3.addLayout(self.hLayout3center)
        self.hLayout3.addStretch(2)
        self.hLayout3.addLayout(self.hLayout3right)
        self.hLayout3.addStretch(1)

        # composizione hLayout4
        self.transpLabel = QLabel()
        self.transpLabel.setFixedHeight(7)
        self.hLayout4.addWidget(self.transpLabel)

        # putting all togheter
        self.vLayout.addLayout(self.hLayout1)
        self.vLayout.addLayout(self.hLayout4)
        self.vLayout.addLayout(self.hLayout2)
        self.vLayout.addLayout(self.hLayout3)

        # calcola medie e voto partenza
        self.SetActualValues()

        # set arrow cursor and checker for modifies
        self.modified = False # if become true ask the user if he want to save changes
        self.index = 1
        eval(f'self.lineName_{self.index}_0.setFocus()')

        self.move(WINDOW_XPOS,WINDOW_YPOS)
        self.setStyleSheet("background-color: #66FF66;")
        self.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.show()

    def closeEvent(self, event):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStyleSheet("background-color: #66FF66;")
        msgBox.setWindowTitle(" ")
        if self.modified == True:
            msgBox.setText("E' stato chiesto di uscire.")
            msgBox.setInformativeText("Vuoi salvare le modifiche?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel);
            msgBox.setDefaultButton(QMessageBox.Save);
        # else:
            # msgBox.setText("Vuoi uscire?")
            # msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            # msgBox.setDefaultButton(QMessageBox.Yes);

        if self.modified == True:
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Save:
                f = open(self.votiPath,'w+')
                for elem in self.matrix:
                    f.write(f"{elem[0]},{elem[1]},{elem[2]}\n")
                f.close()
                f = open(self.votifinPath,'w+')
                for elem in self.matrix_fin:
                    f.write(f"{elem[0]},{elem[1]},{elem[2]}\n")
                f.close()
                print('SAVE clicked')
            # if returnValue == QMessageBox.Discard:
                # print('DISCARD clicked')
            if returnValue == QMessageBox.Cancel:
                event.ignore()
                # print('CANCEL clicked')
            if returnValue == QMessageBox.No:
                event.ignore()
                # print('NO clicked')
            # if returnValue == QMessageBox.Yes:
                # print('YES clicked')

    def AnyOfLineEditHasFocus(self):
        flag = False
        string = ""
        index = 0
        for i in range(1,14):
            flag = eval(f'self.lineName_{i}_0.hasFocus()')
            if flag == True:
                string = "Name"
                index = i
                break
            flag = eval(f'self.lineCfu_{i}_1.hasFocus()')
            if flag == True:
                string = "Cfu"
                index = i
                break
            flag = eval(f'self.lineVoto_{i}_2.hasFocus()')
            if flag == True:
                string = "Voto"
                index = i
                break
            flag = eval(f'self.lineNameFin_{i}_0.hasFocus()')
            if flag == True:
                string = "NameFin"
                index = i
                break
            flag = eval(f'self.lineCfuFin_{i}_1.hasFocus()')
            if flag == True:
                string = "CfuFin"
                index = i
                break
            flag = eval(f'self.lineVotoFin_{i}_2.hasFocus()')
            if flag == True:
                string = "VotoFin"
                index = i
                break
        return index,string

    def keyPressEvent(self, e):
        self.index,string = self.AnyOfLineEditHasFocus()
        if string != "":
            if e.key() == QtCore.Qt.Key_Up and self.index > 1:
                self.index = self.index - 1
            elif e.key() == QtCore.Qt.Key_Down and self.index < 13:
                self.index = self.index + 1
            if string == "Name":
                eval(f'self.lineName_{self.index}_0.setFocus()')
            elif string == "Cfu":
                eval(f'self.lineCfu_{self.index}_1.setFocus()')
            elif string == "Voto":
                eval(f'self.lineVoto_{self.index}_2.setFocus()')
            if string == "NameFin":
                eval(f'self.lineNameFin_{self.index}_0.setFocus()')
            elif string == "CfuFin":
                eval(f'self.lineCfuFin_{self.index}_1.setFocus()')
            elif string == "VotoFin":
                eval(f'self.lineVotoFin_{self.index}_2.setFocus()')

    def MatrixFromFile(self,name):
        with open(name) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        lst = []
        for row in content:
            name,cfu,course = row.split(",")
            lst.append([name,cfu,course])
        return lst

    # def PrintMatrix(self):
        # print(f"modified = {self.modified}")
        # for elem in self.matrix:
            # print(elem)

    def TabChanged(self):
        self.SetActualValues()

    def SetActualValues(self):
        sum_cfu = 0
        sum_vote = 0
        sum_vote_weighted = 0
        n_subjects = 0
        for i in range(1,14):
            name = ""
            cfu = ""
            voto = ""
            if self.tabWid.currentIndex() == 0: # tab ATTUALE
                name = eval(f'self.lineName_{i}_0.text()')
                cfu = eval(f'self.lineCfu_{i}_1.text()')
                voto = eval(f'self.lineVoto_{i}_2.text()')
                self.matrix[i-1][0] = name
                self.matrix[i-1][1] = cfu
                self.matrix[i-1][2] = voto
            else:                               # tab PREVISIONE
                name = eval(f'self.lineNameFin_{i}_0.text()')
                cfu = eval(f'self.lineCfuFin_{i}_1.text()')
                voto = eval(f'self.lineVotoFin_{i}_2.text()')
                self.matrix_fin[i-1][0] = name
                self.matrix_fin[i-1][1] = cfu
                self.matrix_fin[i-1][2] = voto
            if voto != "-":
                sum_cfu = sum_cfu + int(cfu)
                sum_vote = sum_vote + int(voto)
                sum_vote_weighted = sum_vote_weighted + int(voto)*int(cfu)
                n_subjects = n_subjects + 1
            if sum_vote != 0:
                av = round(sum_vote/n_subjects,4)
                self.lineEdit_media_aritm.setText(str(av))
            else:
                self.lineEdit_media_aritm.setText("-")
            if sum_vote_weighted != 0:
                av = round(sum_vote_weighted/sum_cfu,4)
                self.lineEdit_media_pond.setText(str(av))
                av = round(av*110/30)
                self.lineEdit_partenza_laurea.setText(str(av))
            else:
                self.lineEdit_media_pond.setText("-")
                self.lineEdit_partenza_laurea.setText("-")

    def CodeForLineName(self,i):
        code = """
name = eval(f'self.lineName_{i}_0_firstValue')
new_name = str()
if eval(f'self.lineName_{i}_0.text()') == "":
    eval(f'self.lineName_{i}_0.setText(name)')
    # eval(f'self.lineName_{i}_0.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineName_1_0(self):
        self.CodeForLineName(1)
        if self.lineName_1_0_firstValue != self.lineName_1_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_1_0_firstValue = self.lineName_1_0.text()

    def CheckForNumberOnLineName_2_0(self):
        self.CodeForLineName(2)
        if self.lineName_2_0_firstValue != self.lineName_2_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_2_0_firstValue = self.lineName_2_0.text()

    def CheckForNumberOnLineName_3_0(self):
        self.CodeForLineName(3)
        if self.lineName_3_0_firstValue != self.lineName_3_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_3_0_firstValue = self.lineName_3_0.text()

    def CheckForNumberOnLineName_4_0(self):
        self.CodeForLineName(4)
        if self.lineName_4_0_firstValue != self.lineName_4_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_4_0_firstValue = self.lineName_4_0.text()

    def CheckForNumberOnLineName_5_0(self):
        self.CodeForLineName(5)
        if self.lineName_5_0_firstValue != self.lineName_5_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_5_0_firstValue = self.lineName_5_0.text()

    def CheckForNumberOnLineName_6_0(self):
        self.CodeForLineName(6)
        if self.lineName_6_0_firstValue != self.lineName_6_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_6_0_firstValue = self.lineName_6_0.text()

    def CheckForNumberOnLineName_7_0(self):
        self.CodeForLineName(7)
        if self.lineName_7_0_firstValue != self.lineName_7_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_7_0_firstValue = self.lineName_7_0.text()

    def CheckForNumberOnLineName_8_0(self):
        self.CodeForLineName(8)
        if self.lineName_8_0_firstValue != self.lineName_8_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_8_0_firstValue = self.lineName_8_0.text()

    def CheckForNumberOnLineName_9_0(self):
        self.CodeForLineName(9)
        if self.lineName_9_0_firstValue != self.lineName_9_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_9_0_firstValue = self.lineName_9_0.text()

    def CheckForNumberOnLineName_10_0(self):
        self.CodeForLineName(10)
        if self.lineName_10_0_firstValue != self.lineName_10_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_10_0_firstValue = self.lineName_10_0.text()

    def CheckForNumberOnLineName_11_0(self):
        self.CodeForLineName(11)
        if self.lineName_11_0_firstValue != self.lineName_11_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_11_0_firstValue = self.lineName_11_0.text()

    def CheckForNumberOnLineName_12_0(self):
        self.CodeForLineName(12)
        if self.lineName_12_0_firstValue != self.lineName_12_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_12_0_firstValue = self.lineName_12_0.text()

    def CheckForNumberOnLineName_13_0(self):
        self.CodeForLineName(13)
        if self.lineName_13_0_firstValue != self.lineName_13_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineName_13_0_firstValue = self.lineName_13_0.text()

    def CodeForLineCfu(self,i):
        code = """
cfu = int(eval(f'self.lineCfu_{i}_1_firstValue'))
new_cfu = int()
if eval(f'self.lineCfu_{i}_1.text()') != "":
    try:
        new_cfu = int(eval(f'self.lineCfu_{i}_1.text()'))
        if new_cfu < 1:
            eval(f'self.lineCfu_{i}_1.setText(str(cfu))')
            # eval(f'self.lineCfu_{i}_1.setFocus()')
            print("errorNewCfu<1\a")
    except:
        eval(f'self.lineCfu_{i}_1.setText(str(cfu))')
        # eval(f'self.lineCfu_{i}_1.setFocus()')
        print("\a")
else:
    eval(f'self.lineCfu_{i}_1.setText(str(cfu))')
    # eval(f'self.lineCfu_{i}_1.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineCfu_1_1(self):
        self.CodeForLineCfu(1)
        if self.lineCfu_1_1_firstValue != self.lineCfu_1_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_1_1_firstValue = self.lineCfu_1_1.text()

    def CheckForNumberOnLineCfu_2_1(self):
        self.CodeForLineCfu(2)
        if self.lineCfu_2_1_firstValue != self.lineCfu_2_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_2_1_firstValue = self.lineCfu_2_1.text()

    def CheckForNumberOnLineCfu_3_1(self):
        self.CodeForLineCfu(3)
        if self.lineCfu_3_1_firstValue != self.lineCfu_3_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_3_1_firstValue = self.lineCfu_3_1.text()

    def CheckForNumberOnLineCfu_4_1(self):
        self.CodeForLineCfu(4)
        if self.lineCfu_4_1_firstValue != self.lineCfu_4_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_4_1_firstValue = self.lineCfu_4_1.text()

    def CheckForNumberOnLineCfu_5_1(self):
        self.CodeForLineCfu(5)
        if self.lineCfu_5_1_firstValue != self.lineCfu_5_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_5_1_firstValue = self.lineCfu_5_1.text()

    def CheckForNumberOnLineCfu_6_1(self):
        self.CodeForLineCfu(6)
        if self.lineCfu_6_1_firstValue != self.lineCfu_6_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_6_1_firstValue = self.lineCfu_6_1.text()

    def CheckForNumberOnLineCfu_7_1(self):
        self.CodeForLineCfu(7)
        if self.lineCfu_7_1_firstValue != self.lineCfu_7_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_7_1_firstValue = self.lineCfu_7_1.text()

    def CheckForNumberOnLineCfu_8_1(self):
        self.CodeForLineCfu(8)
        if self.lineCfu_8_1_firstValue != self.lineCfu_8_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_8_1_firstValue = self.lineCfu_8_1.text()

    def CheckForNumberOnLineCfu_9_1(self):
        self.CodeForLineCfu(9)
        if self.lineCfu_9_1_firstValue != self.lineCfu_9_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_9_1_firstValue = self.lineCfu_9_1.text()

    def CheckForNumberOnLineCfu_10_1(self):
        self.CodeForLineCfu(10)
        if self.lineCfu_10_1_firstValue != self.lineCfu_10_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_10_1_firstValue = self.lineCfu_10_1.text()

    def CheckForNumberOnLineCfu_11_1(self):
        self.CodeForLineCfu(11)
        if self.lineCfu_11_1_firstValue != self.lineCfu_11_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_11_1_firstValue = self.lineCfu_11_1.text()

    def CheckForNumberOnLineCfu_12_1(self):
        self.CodeForLineCfu(12)
        if self.lineCfu_12_1_firstValue != self.lineCfu_12_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_12_1_firstValue = self.lineCfu_12_1.text()

    def CheckForNumberOnLineCfu_13_1(self):
        self.CodeForLineCfu(13)
        if self.lineCfu_13_1_firstValue != self.lineCfu_13_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfu_13_1_firstValue = self.lineCfu_13_1.text()

    def CodeForLineVoto(self,i):
        code = """
voto = eval(f'self.lineVoto_{i}_2_firstValue')
new_voto = str()
if eval(f'self.lineVoto_{i}_2.text()') != "":
    try:
        new_voto = eval(f'self.lineVoto_{i}_2.text()')
        if new_voto == "-":
            eval(f'self.lineVoto_{i}_2.setText(new_voto)')
        elif int(new_voto) < 18 or int(new_voto) > 30:
            eval(f'self.lineVoto_{i}_2.setText(voto)')
            # eval(f'self.lineVoto_{i}_2.setFocus()')
            print("errorNewVoto\a")
    except:
        eval(f'self.lineVoto_{i}_2.setText(voto)')
        # eval(f'self.lineVoto_{i}_2.setFocus()')
        print("\a")
else:
    eval(f'self.lineVoto_{i}_2.setText(voto)')
    # eval(f'self.lineVoto_{i}_2.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineVoto_1_2(self):
        self.CodeForLineVoto(1)
        if self.lineVoto_1_2_firstValue != self.lineVoto_1_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_1_2_firstValue = self.lineVoto_1_2.text()

    def CheckForNumberOnLineVoto_2_2(self):
        self.CodeForLineVoto(2)
        if self.lineVoto_2_2_firstValue != self.lineVoto_2_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_2_2_firstValue = self.lineVoto_2_2.text()

    def CheckForNumberOnLineVoto_3_2(self):
        self.CodeForLineVoto(3)
        if self.lineVoto_3_2_firstValue != self.lineVoto_3_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_3_2_firstValue = self.lineVoto_3_2.text()

    def CheckForNumberOnLineVoto_4_2(self):
        self.CodeForLineVoto(4)
        if self.lineVoto_4_2_firstValue != self.lineVoto_4_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_4_2_firstValue = self.lineVoto_4_2.text()

    def CheckForNumberOnLineVoto_5_2(self):
        self.CodeForLineVoto(5)
        if self.lineVoto_5_2_firstValue != self.lineVoto_5_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_5_2_firstValue = self.lineVoto_5_2.text()

    def CheckForNumberOnLineVoto_6_2(self):
        self.CodeForLineVoto(6)
        if self.lineVoto_6_2_firstValue != self.lineVoto_6_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_6_2_firstValue = self.lineVoto_6_2.text()

    def CheckForNumberOnLineVoto_7_2(self):
        self.CodeForLineVoto(7)
        if self.lineVoto_7_2_firstValue != self.lineVoto_7_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_7_2_firstValue = self.lineVoto_7_2.text()

    def CheckForNumberOnLineVoto_8_2(self):
        self.CodeForLineVoto(8)
        if self.lineVoto_8_2_firstValue != self.lineVoto_8_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_8_2_firstValue = self.lineVoto_8_2.text()

    def CheckForNumberOnLineVoto_9_2(self):
        self.CodeForLineVoto(9)
        if self.lineVoto_9_2_firstValue != self.lineVoto_9_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_9_2_firstValue = self.lineVoto_9_2.text()

    def CheckForNumberOnLineVoto_10_2(self):
        self.CodeForLineVoto(10)
        if self.lineVoto_10_2_firstValue != self.lineVoto_10_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_10_2_firstValue = self.lineVoto_10_2.text()

    def CheckForNumberOnLineVoto_11_2(self):
        self.CodeForLineVoto(11)
        if self.lineVoto_11_2_firstValue != self.lineVoto_11_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_11_2_firstValue = self.lineVoto_11_2.text()

    def CheckForNumberOnLineVoto_12_2(self):
        self.CodeForLineVoto(12)
        if self.lineVoto_12_2_firstValue != self.lineVoto_12_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_12_2_firstValue = self.lineVoto_12_2.text()

    def CheckForNumberOnLineVoto_13_2(self):
        self.CodeForLineVoto(13)
        if self.lineVoto_13_2_firstValue != self.lineVoto_13_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVoto_13_2_firstValue = self.lineVoto_13_2.text()


    # PREVISIONE

    def CodeForLineNameFin(self,i):
        code = """
name = eval(f'self.lineNameFin_{i}_0_firstValue')
new_name = str()
if eval(f'self.lineNameFin_{i}_0.text()') == "":
    eval(f'self.lineNameFin_{i}_0.setText(name)')
    # eval(f'self.lineNameFin_{i}_0.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineNameFin_1_0(self):
        self.CodeForLineNameFin(1)
        if self.lineNameFin_1_0_firstValue != self.lineNameFin_1_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_1_0_firstValue = self.lineNameFin_1_0.text()

    def CheckForNumberOnLineNameFin_2_0(self):
        self.CodeForLineNameFin(2)
        if self.lineNameFin_2_0_firstValue != self.lineNameFin_2_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_2_0_firstValue = self.lineNameFin_2_0.text()

    def CheckForNumberOnLineNameFin_3_0(self):
        self.CodeForLineNameFin(3)
        if self.lineNameFin_3_0_firstValue != self.lineNameFin_3_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_3_0_firstValue = self.lineNameFin_3_0.text()

    def CheckForNumberOnLineNameFin_4_0(self):
        self.CodeForLineNameFin(4)
        if self.lineNameFin_4_0_firstValue != self.lineNameFin_4_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_4_0_firstValue = self.lineNameFin_4_0.text()

    def CheckForNumberOnLineNameFin_5_0(self):
        self.CodeForLineNameFin(5)
        if self.lineNameFin_5_0_firstValue != self.lineNameFin_5_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_5_0_firstValue = self.lineNameFin_5_0.text()

    def CheckForNumberOnLineNameFin_6_0(self):
        self.CodeForLineNameFin(6)
        if self.lineNameFin_6_0_firstValue != self.lineNameFin_6_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_6_0_firstValue = self.lineNameFin_6_0.text()

    def CheckForNumberOnLineNameFin_7_0(self):
        self.CodeForLineNameFin(7)
        if self.lineNameFin_7_0_firstValue != self.lineNameFin_7_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_7_0_firstValue = self.lineNameFin_7_0.text()

    def CheckForNumberOnLineNameFin_8_0(self):
        self.CodeForLineNameFin(8)
        if self.lineNameFin_8_0_firstValue != self.lineNameFin_8_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_8_0_firstValue = self.lineNameFin_8_0.text()

    def CheckForNumberOnLineNameFin_9_0(self):
        self.CodeForLineNameFin(9)
        if self.lineNameFin_9_0_firstValue != self.lineNameFin_9_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_9_0_firstValue = self.lineNameFin_9_0.text()

    def CheckForNumberOnLineNameFin_10_0(self):
        self.CodeForLineNameFin(10)
        if self.lineNameFin_10_0_firstValue != self.lineNameFin_10_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_10_0_firstValue = self.lineNameFin_10_0.text()

    def CheckForNumberOnLineNameFin_11_0(self):
        self.CodeForLineNameFin(11)
        if self.lineNameFin_11_0_firstValue != self.lineNameFin_11_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_11_0_firstValue = self.lineNameFin_11_0.text()

    def CheckForNumberOnLineNameFin_12_0(self):
        self.CodeForLineNameFin(12)
        if self.lineNameFin_12_0_firstValue != self.lineNameFin_12_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_12_0_firstValue = self.lineNameFin_12_0.text()

    def CheckForNumberOnLineNameFin_13_0(self):
        self.CodeForLineNameFin(13)
        if self.lineNameFin_13_0_firstValue != self.lineNameFin_13_0.text():
            self.modified = True
            self.SetActualValues()
            self.lineNameFin_13_0_firstValue = self.lineNameFin_13_0.text()

    def CodeForLineCfuFin(self,i):
        code = """
cfu = int(eval(f'self.lineCfuFin_{i}_1_firstValue'))
new_cfu = int()
if eval(f'self.lineCfuFin_{i}_1.text()') != "":
    try:
        new_cfu = int(eval(f'self.lineCfuFin_{i}_1.text()'))
        if new_cfu < 1:
            eval(f'self.lineCfuFin_{i}_1.setText(str(cfu))')
            # eval(f'self.lineCfuFin_{i}_1.setFocus()')
            print("errorNewCfuFin<1\a")
    except:
        eval(f'self.lineCfuFin_{i}_1.setText(str(cfu))')
        # eval(f'self.lineCfuFin_{i}_1.setFocus()')
        print("\a")
else:
    eval(f'self.lineCfuFin_{i}_1.setText(str(cfu))')
    # eval(f'self.lineCfuFin_{i}_1.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineCfuFin_1_1(self):
        self.CodeForLineCfuFin(1)
        if self.lineCfuFin_1_1_firstValue != self.lineCfuFin_1_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_1_1_firstValue = self.lineCfuFin_1_1.text()

    def CheckForNumberOnLineCfuFin_2_1(self):
        self.CodeForLineCfuFin(2)
        if self.lineCfuFin_2_1_firstValue != self.lineCfuFin_2_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_2_1_firstValue = self.lineCfuFin_2_1.text()

    def CheckForNumberOnLineCfuFin_3_1(self):
        self.CodeForLineCfuFin(3)
        if self.lineCfuFin_3_1_firstValue != self.lineCfuFin_3_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_3_1_firstValue = self.lineCfuFin_3_1.text()

    def CheckForNumberOnLineCfuFin_4_1(self):
        self.CodeForLineCfuFin(4)
        if self.lineCfuFin_4_1_firstValue != self.lineCfuFin_4_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_4_1_firstValue = self.lineCfuFin_4_1.text()

    def CheckForNumberOnLineCfuFin_5_1(self):
        self.CodeForLineCfuFin(5)
        if self.lineCfuFin_5_1_firstValue != self.lineCfuFin_5_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_5_1_firstValue = self.lineCfuFin_5_1.text()

    def CheckForNumberOnLineCfuFin_6_1(self):
        self.CodeForLineCfuFin(6)
        if self.lineCfuFin_6_1_firstValue != self.lineCfuFin_6_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_6_1_firstValue = self.lineCfuFin_6_1.text()

    def CheckForNumberOnLineCfuFin_7_1(self):
        self.CodeForLineCfuFin(7)
        if self.lineCfuFin_7_1_firstValue != self.lineCfuFin_7_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_7_1_firstValue = self.lineCfuFin_7_1.text()

    def CheckForNumberOnLineCfuFin_8_1(self):
        self.CodeForLineCfuFin(8)
        if self.lineCfuFin_8_1_firstValue != self.lineCfuFin_8_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_8_1_firstValue = self.lineCfuFin_8_1.text()

    def CheckForNumberOnLineCfuFin_9_1(self):
        self.CodeForLineCfuFin(9)
        if self.lineCfuFin_9_1_firstValue != self.lineCfuFin_9_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_9_1_firstValue = self.lineCfuFin_9_1.text()

    def CheckForNumberOnLineCfuFin_10_1(self):
        self.CodeForLineCfuFin(10)
        if self.lineCfuFin_10_1_firstValue != self.lineCfuFin_10_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_10_1_firstValue = self.lineCfuFin_10_1.text()

    def CheckForNumberOnLineCfuFin_11_1(self):
        self.CodeForLineCfuFin(11)
        if self.lineCfuFin_11_1_firstValue != self.lineCfuFin_11_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_11_1_firstValue = self.lineCfuFin_11_1.text()

    def CheckForNumberOnLineCfuFin_12_1(self):
        self.CodeForLineCfuFin(12)
        if self.lineCfuFin_12_1_firstValue != self.lineCfuFin_12_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_12_1_firstValue = self.lineCfuFin_12_1.text()

    def CheckForNumberOnLineCfuFin_13_1(self):
        self.CodeForLineCfuFin(13)
        if self.lineCfuFin_13_1_firstValue != self.lineCfuFin_13_1.text():
            self.modified = True
            self.SetActualValues()
            self.lineCfuFin_13_1_firstValue = self.lineCfuFin_13_1.text()

    def CodeForLineVotoFin(self,i):
        code = """
voto = eval(f'self.lineVotoFin_{i}_2_firstValue')
new_voto = str()
if eval(f'self.lineVotoFin_{i}_2.text()') != "":
    try:
        new_voto = eval(f'self.lineVotoFin_{i}_2.text()')
        if new_voto == "-":
            eval(f'self.lineVotoFin_{i}_2.setText(new_voto)')
        elif int(new_voto) < 18 or int(new_voto) > 30:
            eval(f'self.lineVotoFin_{i}_2.setText(voto)')
            # eval(f'self.lineVotoFin_{i}_2.setFocus()')
            print("errorNewVotoFin\a")
    except:
        eval(f'self.lineVotoFin_{i}_2.setText(voto)')
        # eval(f'self.lineVotoFin_{i}_2.setFocus()')
        print("\a")
else:
    eval(f'self.lineVotoFin_{i}_2.setText(voto)')
    # eval(f'self.lineVotoFin_{i}_2.setFocus()')
    print("\a")
"""
        exec(code)

    def CheckForNumberOnLineVotoFin_1_2(self):
        self.CodeForLineVotoFin(1)
        if self.lineVotoFin_1_2_firstValue != self.lineVotoFin_1_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_1_2_firstValue = self.lineVotoFin_1_2.text()

    def CheckForNumberOnLineVotoFin_2_2(self):
        self.CodeForLineVotoFin(2)
        if self.lineVotoFin_2_2_firstValue != self.lineVotoFin_2_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_2_2_firstValue = self.lineVotoFin_2_2.text()

    def CheckForNumberOnLineVotoFin_3_2(self):
        self.CodeForLineVotoFin(3)
        if self.lineVotoFin_3_2_firstValue != self.lineVotoFin_3_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_3_2_firstValue = self.lineVotoFin_3_2.text()

    def CheckForNumberOnLineVotoFin_4_2(self):
        self.CodeForLineVotoFin(4)
        if self.lineVotoFin_4_2_firstValue != self.lineVotoFin_4_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_4_2_firstValue = self.lineVotoFin_4_2.text()

    def CheckForNumberOnLineVotoFin_5_2(self):
        self.CodeForLineVotoFin(5)
        if self.lineVotoFin_5_2_firstValue != self.lineVotoFin_5_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_5_2_firstValue = self.lineVotoFin_5_2.text()

    def CheckForNumberOnLineVotoFin_6_2(self):
        self.CodeForLineVotoFin(6)
        if self.lineVotoFin_6_2_firstValue != self.lineVotoFin_6_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_6_2_firstValue = self.lineVotoFin_6_2.text()

    def CheckForNumberOnLineVotoFin_7_2(self):
        self.CodeForLineVotoFin(7)
        if self.lineVotoFin_7_2_firstValue != self.lineVotoFin_7_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_7_2_firstValue = self.lineVotoFin_7_2.text()

    def CheckForNumberOnLineVotoFin_8_2(self):
        self.CodeForLineVotoFin(8)
        if self.lineVotoFin_8_2_firstValue != self.lineVotoFin_8_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_8_2_firstValue = self.lineVotoFin_8_2.text()

    def CheckForNumberOnLineVotoFin_9_2(self):
        self.CodeForLineVotoFin(9)
        if self.lineVotoFin_9_2_firstValue != self.lineVotoFin_9_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_9_2_firstValue = self.lineVotoFin_9_2.text()

    def CheckForNumberOnLineVotoFin_10_2(self):
        self.CodeForLineVotoFin(10)
        if self.lineVotoFin_10_2_firstValue != self.lineVotoFin_10_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_10_2_firstValue = self.lineVotoFin_10_2.text()

    def CheckForNumberOnLineVotoFin_11_2(self):
        self.CodeForLineVotoFin(11)
        if self.lineVotoFin_11_2_firstValue != self.lineVotoFin_11_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_11_2_firstValue = self.lineVotoFin_11_2.text()

    def CheckForNumberOnLineVotoFin_12_2(self):
        self.CodeForLineVotoFin(12)
        if self.lineVotoFin_12_2_firstValue != self.lineVotoFin_12_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_12_2_firstValue = self.lineVotoFin_12_2.text()

    def CheckForNumberOnLineVotoFin_13_2(self):
        self.CodeForLineVotoFin(13)
        if self.lineVotoFin_13_2_firstValue != self.lineVotoFin_13_2.text():
            self.modified = True
            self.SetActualValues()
            self.lineVotoFin_13_2_firstValue = self.lineVotoFin_13_2.text()


def create_file(file2create):
    with open(file2create,'w+') as f:
        f.write("AUTOMATA AND QUEUEING SYSTEMS,6,-\n")
        f.write("HIGH PERFORMANCE COMPUTER ARCHITECTURE,9,-\n")
        f.write("ADVANCED DIGITAL IMAGE PROCESSING,9,-\n")
        f.write("MACHINE LEARNING,6,-\n")
        f.write("ARTIFICIAL INTELLIGENCE,9,-\n")
        f.write("BIG DATA,6,-\n")
        f.write("MODELS AND LANGUAGES FOR BIOINFORMATICS,6,-\n")
        f.write("NETWORK OPTIMIZATION,6,-\n")
        f.write("DESIGN OF APPLICATIONS SERVICES AND SYSTEMS,9,-\n")
        f.write("?????????????????????????????????,6,-\n")
        f.write("?????????????????????????????????,6,-\n")
        f.write("?????????????????????????????????,6,-\n")
        f.write("?????????????????????????????????,6,-\n")

if __name__ == '__main__':

    # create the $HOME/.inginf-GUI directory if it not exist 
    user_home = str(Path.home())
    dir_to_create = Path(user_home+"/.inginf-GUI")
    if dir_to_create.is_dir():
        print(f"{str(dir_to_create)} already exist")
    else:
        try:
            os.makedirs(str(dir_to_create))
        except OSError:
            print (f"Creation of the directory {str(dir_to_create)} failed")
        else:
            print (f"Successfully created the directory {str(dir_to_create)}")
    # create the files voti e votifin if they not exists
    file_to_create1 = Path(str(dir_to_create)+"/voti.txt")
    if not file_to_create1.is_file():
        create_file(str(file_to_create1))
    file_to_create2 = Path(str(dir_to_create)+"/votifin.txt")
    if not file_to_create2.is_file():
        create_file(str(file_to_create2))

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    window = Window(str(file_to_create1),str(file_to_create2))

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

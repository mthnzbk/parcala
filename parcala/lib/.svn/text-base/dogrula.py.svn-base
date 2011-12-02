# -*- coding:utf-8 -*-

#Copyright (C) 2011, Metehan Özbek
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtGui import QDialog, QGridLayout, QSizePolicy, QSpacerItem, QPushButton, QComboBox, QFileDialog, QMessageBox, QLineEdit
from PyQt4.QtCore import QDir, QSize, QFile
from karawidget import KaraWidget

class DogrulaDialog(QDialog):
    def __init__(self, ui):
        QDialog.__init__(self, ui)
        self.ui = ui
        self.resize(450, 170)
        self.setMinimumSize(QSize(450, 170))
        self.setMaximumSize(QSize(500, 200))
        self.setWindowTitle(self.trUtf8("Doğrula"))

        self.gridLayout = QGridLayout(self)

        self.neredenButton = QPushButton(self)
        self.neredenButton.setText(self.trUtf8("Nereden"))
        self.neredenButton.clicked.connect(self.nereden)
        self.gridLayout.addWidget(self.neredenButton, 0, 4, 1, 1)

        self.dogrulaButton = QPushButton(self)
        self.dogrulaButton.setText(self.trUtf8("Doğrula"))
        self.dogrulaButton.clicked.connect(self.dogrula)
        self.gridLayout.addWidget(self.dogrulaButton, 3, 4, 1, 1)

        self.neredenEdit = QLineEdit(self)
        self.neredenEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.neredenEdit, 0, 0, 1, 4)

        self.hashEdit = QLineEdit(self)
        self.hashEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.hashEdit, 3, 2, 1, 1)

        spacerItem = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        
        self.comboBox = QComboBox(self)
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.addItem("MD5")
        self.comboBox.addItem("SHA1")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.karaWidget = KaraWidget(self, "=")
        self.karaWidget.hide()

    def nereden(self):
        dosya = QFileDialog.getOpenFileName(self, "", QDir.homePath())
        if dosya == "":
            pass
        elif QFile.exists(dosya):
            self.neredenEdit.setText(dosya)
        else:
            QMessageBox.warning(self, self.trUtf8("Hata!"), self.trUtf8("Böyle bir dosya mevcut değil!"))

    def dogrula(self):
        if self.neredenEdit.text() == "":
            QMessageBox.warning(self, self.trUtf8("Hata!"), self.trUtf8("Dosya seçmediniz!"))
        else:
            self.karaWidget.show()
            self.karaWidget.start()

    def keyPressEvent(self, event):
        pass

    def resizeEvent(self, event):
        self.karaWidget.setGeometry(0,0, event.size().width(), event.size().height())


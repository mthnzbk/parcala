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

from PyQt4.QtGui import QDialog, QGridLayout, QSizePolicy, QSpacerItem, QPushButton, QFileDialog, QMessageBox, QLineEdit
from PyQt4.QtCore import QDir, QSize, QFile
from karawidget import KaraWidget

class BirlestirDialog(QDialog):
    def __init__(self, ui):
        QDialog.__init__(self, ui)
        self.ui = ui
        self.resize(450, 170)
        self.setMinimumSize(QSize(450, 170))
        self.setMaximumSize(QSize(500, 200))
        self.setWindowTitle(self.trUtf8("Birleştir"))
        self.gridLayout = QGridLayout(self)

        self.neredenButton = QPushButton(self)
        self.neredenButton.setText(self.trUtf8("Nereden"))
        self.neredenButton.clicked.connect(self.nereden)
        self.gridLayout.addWidget(self.neredenButton, 0, 3, 1, 1)

        self.nereyeButton = QPushButton(self)
        self.nereyeButton.setText(self.trUtf8("Nereye"))
        self.nereyeButton.clicked.connect(self.nereye)
        self.gridLayout.addWidget(self.nereyeButton, 2, 3, 1, 1)

        self.birlestirButton = QPushButton(self)
        self.birlestirButton.setText(self.trUtf8("Birleştir"))
        self.birlestirButton.clicked.connect(self.birlestir)
        self.gridLayout.addWidget(self.birlestirButton, 5, 3, 1, 1)

        self.neredenEdit = QLineEdit(self)
        self.neredenEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.neredenEdit, 0, 0, 1, 3)

        self.nereyeEdit = QLineEdit(self)
        self.nereyeEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.nereyeEdit, 2, 0, 1, 3)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)

        self.karaWidget = KaraWidget(self, "+")
        self.karaWidget.hide()


    def nereden(self):
        dosya = QFileDialog.getOpenFileName(self, u"", QDir.homePath(), self.trUtf8("001 Dosyası (*.001)"))
        if dosya == "":
            pass
        elif QFile.exists(dosya):
            self.neredenEdit.setText(dosya)
            self.nereyeEdit.setText(u"%s"%dosya[:-4])
        else:
            QMessageBox.warning(self, self.trUtf8("Hata!"), self.trUtf8("Böyle bir dosya mevcut değil!"))

    def nereye(self):
        dosya = QFileDialog.getSaveFileName(self, "", QDir.homePath())
        if not dosya == "":
            self.nereyeEdit.setText(dosya)

    def birlestir(self):
        if self.neredenEdit.text() == "":
            QMessageBox.warning(self, self.trUtf8("Hata!"), self.trUtf8("Dosya seçmediniz!"))
        else:
            self.karaWidget.show()
            self.karaWidget.start()

    def keyPressEvent(self, event):
        pass

    def resizeEvent(self, event):
        self.karaWidget.setGeometry(0,0, event.size().width(), event.size().height())
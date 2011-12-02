#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from PyQt4.QtCore import Qt, QSize, QLocale, QTranslator
from PyQt4.QtGui import QWidget, QApplication, QIcon, QPixmap, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from lib import *

import sys
import resource

class Parcala(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(350, 225)
        self.setMinimumSize(QSize(350, 225))
        self.setMaximumSize(QSize(400, 250))
        self.setWindowTitle(QApplication.applicationName()+" "+QApplication.applicationVersion())

        icon = QIcon()
        icon.addPixmap(QPixmap(":/resim/parcala.png"))
        self.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self)

        self.parcalaButton = QPushButton(self)
        self.parcalaButton.setMinimumSize(QSize(150, 50))
        self.parcalaButton.setText(self.trUtf8("Parçala"))
        self.parcalaButton.clicked.connect(self.parcala)
        self.gridLayout.addWidget(self.parcalaButton, 3, 0, 1, 1)

        self.birlestirButton = QPushButton(self)
        self.birlestirButton.setMinimumSize(QSize(150, 50))
        self.birlestirButton.setText(self.trUtf8("Birleştir"))
        self.birlestirButton.clicked.connect(self.birlestir)
        self.gridLayout.addWidget(self.birlestirButton, 3, 2, 1, 1)

        self.dogrulaButton = QPushButton(self)
        self.dogrulaButton.setMinimumSize(QSize(150, 50))
        self.dogrulaButton.setText(self.trUtf8("Doğrula"))
        self.dogrulaButton.clicked.connect(self.dogrula)
        self.gridLayout.addWidget(self.dogrulaButton, 7, 0, 1, 1)

        self.hakkindaButton = QPushButton(self)
        self.hakkindaButton.setMinimumSize(QSize(150, 50))
        self.hakkindaButton.setText(self.trUtf8("Hakkında"))
        self.hakkindaButton.clicked.connect(self.hakkinda)
        self.gridLayout.addWidget(self.hakkindaButton, 7, 2, 1, 1)

        self.bilgiLabel = QLabel(self)
        self.bilgiLabel.setText(self.trUtf8(u"%s %s \u00a9 2011 - www.metehan.us"%(QApplication.applicationName(),QApplication.applicationVersion())))
        self.bilgiLabel.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.bilgiLabel, 9, 0, 1, 3)
        
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 1)


    def hakkinda(self):
        h = Hakkinda(self)
        h.show()

    def dogrula(self):
        d = DogrulaDialog(self)
        d.show()

    def parcala(self):
        d = ParcalaDialog(self)
        d.show()

    def birlestir(self):
        d = BirlestirDialog(self)
        d.show()

def main():
    from os.path import join, abspath, dirname
    mainPath = abspath(dirname(__file__))
    app = QApplication(sys.argv)
    locale = QLocale.system().name()
    translator = QTranslator()
    translator.load(join(mainPath, "language", "%s"%locale))
    app.installTranslator(translator)
    app.setApplicationName(u"Parçala")
    app.setApplicationVersion("1.8")
    
    pencere = Parcala()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
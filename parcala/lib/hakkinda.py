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

from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QPixmap, QFont, QGroupBox, \
    QScrollArea, QFrame, QWidget, QApplication
from PyQt4.QtCore import Qt



class Hakkinda(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(500, 350)
        self.setMaximumSize(500, 350)
        self.gLayout = QGridLayout(self)
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(":/resim/parcala.png"))
        self.gLayout.addWidget(self.logo, 0, 0, 2, 1)
        self.appName = QLabel(self)
        font = QFont()
        font.setPointSize(32)
        font.setWeight(50)
        self.appName.setFont(font)
        self.gLayout.addWidget(self.appName, 0, 1, 1, 2)
        self.appVersion = QLabel(self)
        font = QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.appVersion.setFont(font)
        self.appVersion.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.gLayout.addWidget(self.appVersion, 1, 1, 1, 2)
        self.gBox = QGroupBox(self)
        font = QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.gBox.setFont(font)
        self.gLayout2 = QGridLayout(self.gBox)
        self.scrollArea = QScrollArea(self.gBox)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 476, 199)

        self.gLayout3 = QGridLayout(self.scrollAreaWidgetContents)
        self.appHakkinda = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.appHakkinda.setFont(font)
        self.appHakkinda.setWordWrap(True)
        self.gLayout3.addWidget(self.appHakkinda, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gLayout2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gLayout.addWidget(self.gBox, 2, 0, 2, 4)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gLayout.addItem(spacerItem1, 2, 1, 1, 2)

        self.setWindowTitle(self.trUtf8(u"%s Hakkında"%QApplication.applicationName()))
        self.appName.setText(self.trUtf8(u"%s"%QApplication.applicationName()))
        self.appVersion.setText(self.trUtf8(u"Sürüm %s"%QApplication.applicationVersion()))
        self.gBox.setTitle(self.trUtf8("Hakkında"))
        self.appHakkinda.setText(self.trUtf8("""
        <p>Parçala, Hj-Split ile aynı işi yapan dosya parçalama ve birleştirme yazılımıdır.</p>
        <p>Parçala, büyük boyutlu dosyaları parçalara böldüğü gibi parçalanmış dosyaları birleştirme ve dosyaların doğrulamasını yapabilmektedir.</p>

        <p><b>Geliştirici:</b> Metehan Özbek - <a href='mailto:metehan@metehan.us'>metehan@metehan.us</a></p>
        <p><b>Görsel Çalışma:</b> Yasin Özcan - <a href='mailto:hamfindik@gmail.com'>hamfindik@gmail.com</a></p>
        <p><b>Lisans:</b> GPL v3</p>
        <p></p>"""))


#-*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame, QGridLayout, QLabel, QProgressBar, QSpacerItem, QSizePolicy, QMessageBox
from islem import *


class KaraWidget(QFrame):
    def __init__(self, ui, opt=None):
        QFrame.__init__(self, ui)
        self.ui = ui
        self.option = opt
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.setGeometry(0,0,450,170)

        self.gridLayout = QGridLayout(self)
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label2 = QLabel(self)
        self.label2.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
        self.progressBar = QProgressBar(self)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)



        if self.option == "+":
            self.birlestir = BirlestirThread(self)
            self.birlestir.finished.connect(self.hide)
            self.connect(self.birlestir, SIGNAL("value"), self.progressBar.setValue)
            self.connect(self.birlestir, SIGNAL("durdur"), self.durdur)

        if self.option == "-":
            self.parcala = ParcalaThread(self)
            self.parcala.finished.connect(self.hide)
            self.connect(self.parcala, SIGNAL("value"), self.progressBar.setValue)
            self.connect(self.parcala, SIGNAL("durdur"), self.durdur)

        elif self.option == "=":
            self.dogrula = DogrulaThread(self)
            self.dogrula.finished.connect(self.hide)
            self.connect(self.dogrula, SIGNAL("value"), self.progressBar.setValue)


    def durdur(self):
        if self.option == "-":
            uyari = QMessageBox.warning(None, self.trUtf8("Hata!"), self.trUtf8("Aynı isimde dosya(lar) mevcut."), self.trUtf8("Üzer(ler)ine Yaz"), self.trUtf8("İptal"))
            if not uyari:
                self.parcala.uzerineYaz = True
                self.show()
                self.parcala.start()
            else:
                self.parcala.quit()
                self.hide()

        if self.option == "+":
            uyari = QMessageBox.warning(None, self.trUtf8("Hata!"), self.trUtf8("Aynı isimde dosya mevcut."), self.trUtf8("Üzerine Yaz"), self.trUtf8("İptal"))
            if not uyari:
                self.birlestir.uzerineYaz = True
                self.show()
                self.birlestir.start()
            else:
                self.birlestir.quit()
                self.hide()

    def start(self):
        if self.option == "-":
            self.parcala.start()
        elif self.option == "+":
            self.birlestir.start()
        elif self.option == "=":
            self.dogrula.start()

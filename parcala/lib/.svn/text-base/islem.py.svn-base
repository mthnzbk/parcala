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

from PyQt4.QtCore import QThread, SIGNAL, QFile, QIODevice
from hashlib import md5, sha1
from os.path import dirname, abspath


class DogrulaThread(QThread):
    def __init__(self, ui):
        QThread.__init__(self, ui)
        self.ui = ui

    def run(self):
        dosyaAdi = self.ui.ui.neredenEdit.text()
        dosya = QFile(dosyaAdi)
        dosya.open(QIODevice.ReadOnly)
        oku = 1024*1024
        yuzde = dosya.size()/oku+1
        self.ui.progressBar.setMaximum(yuzde)

        hash = self.ui.ui.comboBox.currentText()

        if hash == "MD5":
            self.sum = md5()
        elif hash == "SHA1":
            self.sum = sha1()

        self.ui.label.setText(dosyaAdi)
        sayac = 0
        while not dosya.atEnd():
            self.sum.update(dosya.read(oku))
            sayac += 1
            self.emit(SIGNAL("value"), sayac)
        self.ui.ui.hashEdit.setText(self.sum.hexdigest())
        self.msleep(500)

class BirlestirThread(QThread):
    def __init__(self, ui):
        QThread.__init__(self, ui)
        self.ui = ui
        self.uzerineYaz = False

    def birlestir(self, dosya):
        import os
        liste = []
        d = dosya[:-3] #uzantısı alınıyor
        yol = abspath(dirname(str(dosya)))
        say = 0
        l = os.listdir(yol)
        while True:
            say += 1
            u = str(say).zfill(3)
            yolsuz = "/".join(str(d+u).split("/")[-1:]) #dosyayı yolundan ayırıyor.
            if yolsuz in  l:
                liste.append(d+u)
            else:
                break
        return liste

    def toplamBoyut(self, liste):
        toplamBoyut = 0
        for i in liste:
            toplamBoyut += QFile(i).size()
        return toplamBoyut

    def run(self):
        self.ui.label.setText(self.ui.ui.nereyeEdit.text())
        dosyaListesi = self.birlestir(self.ui.ui.neredenEdit.text())
        dosyaYaz = QFile(self.ui.ui.nereyeEdit.text())
        if dosyaYaz.exists() and not self.uzerineYaz:
            self.emit(SIGNAL("durdur"))
            return
        dosyaYaz.open(QIODevice.WriteOnly)
        
        oku = 1024*1024
        boyut = self.toplamBoyut(dosyaListesi)/oku
        self.ui.progressBar.setMaximum(boyut)
        sayac = 0
        for i in dosyaListesi:
            self.ui.label2.setText(i)
            dosyaOku = QFile(i)
            dosyaOku.open(QIODevice.ReadOnly)
            while not dosyaOku.atEnd():
                dosyaYaz.writeData(dosyaOku.read(oku))
                sayac += 1
                self.emit(SIGNAL("value"), sayac)
                self.msleep(1)
                if dosyaOku.atEnd(): break
        dosyaYaz.close()
        self.msleep(500)

class ParcalaThread(QThread):
    def __init__(self, ui):
        QThread.__init__(self, ui)
        self.ui = ui
        self.uzerineYaz = False

    def run(self):
        self.ui.label.setText(self.ui.ui.neredenEdit.text())
        dosyaOku = QFile(self.ui.ui.neredenEdit.text())
        dosyaOku.open(QIODevice.ReadOnly)
        oku = 1024*1024
        partBoyutu = int(self.ui.ui.mbEdit.text())
        self.ui.progressBar.setMaximum(dosyaOku.size()/oku)
        partAdi = self.ui.ui.nereyeEdit.text()
        sayac = 0
        partSayici = 1
        while not dosyaOku.atEnd():
            partAdi = "%s%s"%(partAdi[:-3], str(partSayici).zfill(3))
            self.ui.label2.setText(partAdi)
            partSayici += 1
            dosyaYaz = QFile(partAdi)
            if dosyaYaz.exists() and not self.uzerineYaz:
                self.emit(SIGNAL("durdur"))
                return
            dosyaYaz.open(QIODevice.WriteOnly)
            #self.uzerineYaz = False
            for i in range(partBoyutu):
                dosyaYaz.writeData(dosyaOku.read(oku))
                sayac += 1
                self.emit(SIGNAL("value"), sayac)
                self.msleep(1)
                if dosyaOku.atEnd(): break
            dosyaYaz.close()
        self.msleep(500)
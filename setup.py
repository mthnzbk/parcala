#-*- coding:utf-8 -*-

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

from distutils.core import setup


setup(
    name = "parcala",
    packages = ["parcala", "parcala.lib"],
    package_data = {"parcala" : ["resim/*", "language/*"]},
    scripts = ["scripts/parcala"],
    version = "1.8",
    license = "GPL v3",
    description = u"""Parçala, Hj-Split ile aynı işi yapan dosya parçalama ve birleştirme yazılımıdır.

    Parçala, büyük boyutlu dosyaları parçalara böldüğü gibi parçalanmış dosyaları birleştirme ve dosyaların doğrulamasını yapabilmektedir.""",
    author = u"Metehan Özbek",
    author_email = "metehan@metehan.us",
    url = "http://www.metehan.us/",
    download_url = "",
    keywords = ["PyQt4","Hj-Split", "Splitter","Parçala"],
    classifiers = [
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: Turkish",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python",
    ],

)
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import youtube_dl

#link 	= raw_input('Video Linki: ')
#mp3 	= raw_input('Mp3? yes/no:')


class RuttoDownloader():

	#Indir buttonu
	download_button = ''

	#Linki tutar..
	#Input..
	link = ''

	#Panel app..
	app = ''

	#download as mp3?
	mp3_input = ''

	def __init__(self, parent=None):
		self.ui()		

	# Download işlemini yapar
	# @link indirilecek link
	# @return false
	def download(self):

		link_url = str(self.link.text())
		is_mp3 = str(self.mp3_input.text())

		#Mp3 eklensin mi?
		if is_mp3 == 'yes':

			ydl_opts = {
			    'format': 'bestaudio/best',
			    'postprocessors': [{
			        'key': 'FFmpegExtractAudio',
			        'preferredcodec': 'mp3',
			        'preferredquality': '192',
			    }]
			}

		else:
			ydl_opts = {}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([link_url])
	

	#Paneli çiz..
	# ve
	# göster
	def ui(self):

		self.app = QApplication(sys.argv)
		win = QWidget()
		win.resize(450, 150)

		label = QLabel('Video Linki:')

		self.link = QLineEdit()
		self.mp3_input = QLineEdit()
		self.link.setPlaceholderText("YouTube vide Linki") 
		self.mp3_input.setPlaceholderText("Mp3? yes/no") 

		vbox = QVBoxLayout()
		vbox.addWidget(label)
		vbox.addWidget(self.link)
		vbox.addWidget(self.mp3_input)
		vbox.addStretch()
		hbox = QHBoxLayout()

		self.download_button = QPushButton("Indir")
		hbox.addStretch()
		hbox.addWidget(self.download_button)

		vbox.addStretch()
		vbox.addLayout(hbox)
		win.setLayout(vbox)

		QObject.connect(self.download_button, SIGNAL('clicked()'),self.download)

		win.setWindowTitle("Rutto YouTube Downloader")
		win.show()
		sys.exit(self.app.exec_())


Rutto = RuttoDownloader()
#Rutto.download(link);
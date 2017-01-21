#!/usr/bin/python
# -*- coding: utf-8 -*-

import youtube_dl

link 	= raw_input('Video Linki: ')
mp3 	= raw_input('Mp3? yes/no:')

class RuttoDownloader:

	def __init__(self):
		pass

	def download(self, link):

		if mp3 == 'yes':

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
		    ydl.download([link])
		

class Logger:

	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		pass

	def hook(self,d):
		if d['status'] == 'finished':
			print('Done downloading, now converting ...')		

Rutto = RuttoDownloader()
Rutto.download(link);
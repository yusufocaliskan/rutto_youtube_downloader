import youtube_dl

link 	= raw_input('Video Linki: ')

class RuttoDownloader:

	def __init__(self):
		pass

	def download(self, link):

		ydl_opts = {}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([link])
		


Rutto = RuttoDownloader()
Rutto.download(link);
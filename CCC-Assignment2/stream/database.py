import couchdb

class Couchdb:
	def __init__(self, url):
		self.db = couchdb.Server(url)

	def upload(self, data, db_name):
		try:
			self.db[db_name].save(data)
		except:
			print ('Upload error.')

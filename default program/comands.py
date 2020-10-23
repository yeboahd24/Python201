import bark
import sqlite3
db = DatabaseManager('bookmarks.db')

class CreateBookmarksTableCommand(object):
	def execute(self):
		db.create_table('bookmarks', {
			'id': 'integer primary key autoincrement',
			'title': 'text not null',
			'notes': 'text',
			'date_added': 'text not null',
		})

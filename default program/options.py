from datetime import datetime
import sys
import comands

class AddBookmarkCommand(object):
	def execute(self, data):
		data['date_added'] = datetime.utcnow().isoformat()
		db.add('bookmarks', data)
		return 'Bookmark added!.'


class ListBookmarksCommand(object):
	"""db.select returns a cursor you can iterate
		over to get the records
	"""
	def __init__(self, order_by = 'date_added'):
		self.order_by = order_by

	def execute(self):
		return db.select('bookmarks', order_by = self.order_by.fetchall())




class DeleteBookmarksCommand(object):
	"""delete accepts a dictionary of column name, match value pairs"""
	def execute(self, data):
		db.data('bookmarks', {'id': data})
		return 'Bookmark deleted!'

class QuitCommand(object):
	def execute(self):
		sys.exit()


class Option(object):
	"""The optional preparation step to
		call before executing the command
	"""
	def __init__(self, name, command, prep_call = None):
		self.name = name
		self.command = command
		self.prep_call = prep_call

	def choose(self):
		data = self.prep_call() if self.prep_call else None
		message = self.command.execute(data) if data else self.command.execute()
		print(message)

	def __str__(self):
		return self.name

	def print_options(options):
		for shortcut, option in options.items():
			print(f'({shortcut} {option})')
		print()

def option_choice_is_valid(choice, options):
	return choice in options or choice.upper() in options

def get_option_choice(options):
	choice = input('Choose an aption: ')
	while not option_choice_is_valid(choice, options):
		print('Invalid choice')
		choice = input('Choose an option: ')
	return options[choice.upper()]


if __name__ == '__main__':
	options = {
		'A': Option('Add a bookmark', commands.AddBookmarkCommand()),
		'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
		'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
		'D': Option('Delete a bookmark', commands.DeleteBookmarksCommand()),
		'Q': Option('Quit', commands.QuitCommand()),

	}
	print_options(options)

	chosen_option = get_option_choice(options)
	chosen_option.choose()
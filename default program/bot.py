import requests
import json
import configparser as cfg

class telegram_bot(object):
	def __init__(self, config):
		self.token = self.read_token_from_config_file(config)
		self.base = 'https://api.telegram.org/bot{}/'.format(self.token) # base url with token

	def get_updates(self, offset=None):
		url = self.base + "getUpdates?timeout=100"
		if offset:
			url = url + "&offset={}".format(offset + 1)
		r = request.get(url)
		return json.loads(r.content)

	def send_message(self, msg, chat_id):
		url = self.base + "sendMessage?chat_id={}".format(chat_id, msg)
		if msg not None:
			request.get(url)

	def read_toke_from_config_file(config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('creds', 'token')
		



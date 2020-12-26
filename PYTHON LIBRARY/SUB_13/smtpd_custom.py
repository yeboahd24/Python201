import smtpd
import asyncore
# SMTPServer uses asyncore, so to run the server call asyncore.loop().
# A client is needed to demonstrate the server

class CustomSMTPServer(smtpd.SMTPServer):
	def process_message(self, peer, mailfrom, rcpttos, data):
		print('Receiving message from:', peer)
		print('Message addressed from:', mailfrom)
		print('Message addressed to :', rcpttos)
		print('Message length :', len(data))
server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()

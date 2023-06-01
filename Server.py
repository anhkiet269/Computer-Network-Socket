import socket
import threading
import time
import json
from Account import account
from Get import GET

class Server:
	def __init__(self, ADDR):
		self.PORT = 5500
		self.FORMAT = 'utf-8'
		self.LEN = 2048
		self.ADDR = ADDR
		self.acc = account.Account()
		self.login_user_list = []

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print ("Socket successfully created")

		self.s.bind((self.ADDR, self.PORT))
		print ("socket binded to %s" %(self.PORT))

	def login_respond(self, login_check):
		return {'method' : 'login', 'result' : str(login_check)}

	def signup_respond(self, signup_check):
		return {'method' : 'signup', 'result' : str(signup_check)}

	def data_respond(self, login_check):
		if login_check:
			data_obj = data_obj = GET.load_data()
		else:
			data_obj = []

		return {'method' : 'getdata', 'result' : data_obj}

	def login(self, conn, user_data):
		login_check = self.acc.login(user_data)
		print(login_check)

		data_obj = self.login_respond(login_check)
		data_str = json.dumps(data_obj)

		conn.sendall(data_str.encode(self.FORMAT))

		return login_check

	def signup(self, conn, user_data):
		signup_check = self.acc.signup(user_data)
		print(signup_check)

		data_obj = self.signup_respond(signup_check)
		data_str = json.dumps(data_obj)

		conn.sendall(data_str.encode(self.FORMAT))

		return signup_check

	def respondData(self, conn, login_check):
		data_obj = self.data_respond(login_check)
		data_str = json.dumps(data_obj)

		conn.sendall(data_str.encode(self.FORMAT))


	def handle_connect(self, conn, addr):
		login_check = False
		user_name = ''

		while True:
			try:
				data = conn.recv(self.LEN)

				if data:
					data_obj = json.loads(data.decode(self.FORMAT))

					print(data_obj['method'])

					if data_obj['method'] == 'close':
						print("Connection close at", addr)

						if user_name:
							self.login_user_list.remove(user_name)
							self.acc.save_login_user(self.login_user_list)

						break

					elif data_obj['method'] == 'login':
						login_check = self.login(conn, data_obj['userdata'])

						if login_check:
							self.acc.save()

							user_name = data_obj['userdata']['username']
							self.login_user_list.append(user_name)
							self.acc.save_login_user(self.login_user_list)

					elif data_obj['method'] == 'logout':
						login_check = False

						if user_name:
							self.login_user_list.remove(user_name)
							self.acc.save_login_user(self.login_user_list)

						conn.sendall(str(not login_check).encode(self.FORMAT))

					elif data_obj['method'] == 'signup':
						login_check = self.signup(conn, data_obj['userdata'])
						self.acc.test()

					elif data_obj['method'] == 'getdata':
						print(login_check)
						self.respondData(conn, login_check)

			except ConnectionAbortedError:
				print("Lost connection from ", addr)
				break
			# except:
			# 	print('Unknown error!')
			# 	conn.close()
			# 	return

		conn.close()

	def start(self, n):
		self.s.listen(n)     
		print ("socket is listening")

		done = False

		while True: 
			conn, addr = self.s.accept()
			print ('Got connection from', addr )

			thread = threading.Thread(target = self.handle_connect, args = (conn, addr))
			thread.start()
			print('ACTIVE CONNECTION: ', threading.activeCount() - 1)
			
		self.s.close()

	def __del__(self):
		self.acc.save()
		self.acc.save_login_user([])
		self.s.close()

server = Server('0.0.0.0')
server.start(5)
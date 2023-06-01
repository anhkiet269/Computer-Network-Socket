import socket
import json
import time

class Client:
	def __init__(self):
		self.s = socket.socket()         

		self.PORT = 5500
		self.FORMAT = 'utf-8' 
		self.LEN = 2048
		self.ON = False
		self.ADDR = ''

	def connect(self, addr):
		if (addr.find(".") == -1):
			print("Wrong IP address")
			return self.ON

		self.ADDR = addr

		if self.ADDR:
			try:
				self.s.connect((self.ADDR, self.PORT))
				self.ON = True
				print("Connected!")

			except ConnectionRefusedError:
				print("Can't connect to server!")
				self.ON = False
				return self.ON

			except socket.gaierror:
				print("Wrong address!")
				return self.ON

		print(self.ON)
		return self.ON

	def disconnect(self):
		if self.ON:
			self.closeSocket()

		self.ON = False
		self.s.close()

		self.s = socket.socket() 

		print('Disconnected!')

	def login_method(self, user_name, password):
		return {'method' : 'login', 'userdata' : {'username' : user_name, 'password' : password}}

	def signup_method(self, user_name, password):
		return {'method' : 'signup', 'userdata' : {'username' : user_name, 'password' : password}}

	def close_method(self):
		return {'method' : 'close'}

	def login(self, user_name, password):
		data_obj = self.login_method(user_name, password)
		data_str = json.dumps(data_obj)

		try:
			self.s.sendall(data_str.encode(self.FORMAT))
		except ConnectionResetError:
			return False


		r_str = self.s.recv(self.LEN).decode(self.FORMAT)
		r_obj = json.loads(r_str)

		return (r_obj['result'] == 'True')

	def signup(self, user_name, password):
		data_obj = self.signup_method(user_name, password)
		data_str = json.dumps(data_obj)

		try:
			self.s.sendall(data_str.encode(self.FORMAT))
		except ConnectionResetError:
			return False

		r_str = self.s.recv(self.LEN).decode(self.FORMAT)
		r_obj = json.loads(r_str)

		return (r_obj['result'] == 'True')

	def logout(self):
		data_obj = {'method' : 'logout'}
		data_str = json.dumps(data_obj)

		try:
			self.s.sendall(data_str.encode(self.FORMAT))
		except ConnectionResetError:
			return False

		r_str = self.s.recv(self.LEN).decode(self.FORMAT)

		return (r_str == 'True')

	def requestData(self):
		data_obj = {'method' : 'getdata'}
		data_str = json.dumps(data_obj)

		try:
			self.s.sendall(data_str.encode(self.FORMAT))
		except ConnectionResetError:
			return []

		r_str = self.s.recv(self.LEN).decode(self.FORMAT)
		r_obj = json.loads(r_str)

		return r_obj['result']

	def closeSocket(self):
		data_obj = self.close_method()
		data_str = json.dumps(data_obj)
		
		try:
			self.s.sendall(data_str.encode(self.FORMAT))
		except ConnectionResetError:
			return False

	def test(self):
		op = 0

		while True:
			try:
				op = int(input('Input option '))
					
				if op == -1:
					print("Quited!")
					self.closeSocket()
					break

				elif op == 0:
					user_name = input('input user name ')
					password = input('input password ')
					print(self.login(user_name, password))

				elif op == 1:
					user_name = input('input user name ')
					password = input('input password ')
					print(self.signup(user_name, password))

				elif op == 2:
					print(self.logout())
					
				elif op == 3:
					print(self.requestData())

			except ConnectionResetError:
				print('Lost connection form server!')
				break

			except KeyboardInterrupt:
				print("KeyboardInterrupt")
				self.closeSocket()
				break

		self.s.close()

	def __del__(self):
		if self.ON:
			self.closeSocket()

		self.ON = False
		self.s.close()
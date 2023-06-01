import json
import os

class Account:
	def __init__(self):
		self.users_list = self.load_userdata()

	def load_userdata(self):
		with open(os.path.join('Account', 'user_data.json'), 'r') as f:
			users_list = json.load(f)

		return users_list

	def save(self):
		with open(os.path.join('Account', 'user_data.json'), 'w') as g:
			json.dump(self.users_list, g)

	def save_login_user(self, user_name_list):
		with open(os.path.join('Account', 'login_user.json'), 'w') as g:
			json.dump(user_name_list, g)

	def load_login_user(self):
		with open(os.path.join('Account', 'login_user.json'), 'r') as f:
			user_list = json.load(f)

		return user_list

	def signup(self, user_data):
		start = 0
		end = len(self.users_list) - 1

		if end < 0:
			self.users_list.append(user_data)
			return True
		if end == 0 and user_data['username'] == self.users_list[end]['username']:
			return False
		if user_data['username'] > self.users_list[end]['username']:
			self.users_list.append(user_data)
			return True
		if user_data['username'] < self.users_list[start]['username']:
			self.users_list.insert(start, user_data)
			return True
		if user_data['username'] == self.users_list[start]['username']:
			return False

		mid = end

		while mid != start:
			if user_data['username'] == self.users_list[mid]['username']:
				return False

			if user_data['username'] < self.users_list[mid]['username']:
				end = mid
			else:
				start = mid

			mid = (start + end)//2

		self.users_list.insert(mid + 1, user_data)
		return True

	def findUser(self, user_name):
		start = 0
		end = len(self.users_list) - 1

		if end < 0:
			return {}, -1
		if end == 0:
			if user_name == self.users_list[0]['username']:
				return self.users_list[0], 0
			else:
				return {}, -1
		if (end == 1):
			if user_name == self.users_list[0]['username']:
				return self.users_list[0], 0
			elif user_name == self.users_list[1]['username']:
				return self.users_list[1], 1
			else:
				return {}, -1
		if user_name == self.users_list[start]['username']:
			return self.users_list[start], 0

		mid = end

		while mid != start:
			if user_name == self.users_list[mid]['username']:
				return self.users_list[mid], mid

			if user_name < self.users_list[mid]['username']:
				end = mid
			else:
				start = mid

			mid = (start + end)//2

		return {}, -1

	def login(self, user_data):
		my_data, index = self.findUser(user_data['username'])

		if my_data == {}:
			return False
		if user_data['password'] != my_data['password']:
			return False

		return True

	def delete(self, user_data):
		my_data, index = self.findUser(user_data['username'])

		if my_data == {}:
			return False
		if user_data['password'] != my_data['password']:
			return False

		self.users_list.pop(index)

		return True
		
	def test(self):
		print(self.users_list)
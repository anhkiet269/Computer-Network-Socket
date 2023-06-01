from datetime import datetime, timedelta
import os
import json

def load_data():
	with open(os.path.join('Get', 'data.json'), 'r') as f:
		data = json.load(f)

	return data['results']
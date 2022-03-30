from collections import Counter


def get_men_counted_by_year(users):
	men = [i['birthday'][:4] for i in users if i['gender'] == 'male']
	print(dict(Counter(men)))
	return dict(Counter(men))
	
users = [
	{'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
	{'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
	{'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
	{'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
	{'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
	{'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
	{'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
	{'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
	{'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
	{'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
	]	

# Test Program

get_men_counted_by_year(users) # {'1973': 3, '1963': 1, '1980': 2, '2012': 1, '1999': 1}
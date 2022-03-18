def diff_keys(old_dict, new_dict):
	result = {}
	result['kept'] = set(old_dict.keys()) & set(new_dict.keys())
	result['added'] = set(new_dict.keys()) - set(old_dict.keys())
	result['remove'] = set(old_dict.keys()) - set(new_dict.keys())
	print(result)

# Test Program
diff_keys({'name': 'Bob', 'age': 42}, {}) # {'kept': set(), 'added': set(), 'remove': {'name', 'age'}}
diff_keys({}, {'name': 'Bob', 'age': 42}) # {'kept': set(), 'added': {'name', 'age'}, 'remove': set()}
diff_keys({'a': 2}, {'a': 1}) # {'kept': {'a'}, 'added': set(), 'remove': set()}
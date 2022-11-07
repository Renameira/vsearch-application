from functools import wraps

def uppercase_output(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
	return wrapper

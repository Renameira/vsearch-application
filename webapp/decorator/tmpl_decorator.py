
from functools import wraps

def decorator_name(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		# 1. code to execute BEFORE calling the decorated function

		# 2. call the decorated function as required, returning its
		# results if needed

		# 3. Code to execute INSTEAD of calling the decarated function 
	return wrapper

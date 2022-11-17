from flask import session, render_template
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        title = "You are NOT logged in."
        return render_template("message.html", the_title=title)

    return wrapper


def uppercase_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

from flask import session, redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if session.get("username") is None or session.get("if_logged") is None:
        if session.get("if_logged") is None:
            return redirect("/login", code=302)
        return f(*args, **kwargs)
    return decorated_function

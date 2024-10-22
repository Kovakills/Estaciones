from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':  # Verifica si el usuario es admin
            abort(403)  # Prohibido
        return f(*args, **kwargs)
    return decorated_function

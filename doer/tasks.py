from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from doer.auth import login_required
from doer.db import get_db

bp = Blueprint('tasks', __name__)

@bp.route('/')
def index():
	db = get_db()
	all_users = db.execute(
		'SELECT id, username FROM users'
	).fetchall()
	return render_template('auth/users.html', users=all_users)
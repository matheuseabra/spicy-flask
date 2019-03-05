from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from blog.auth import login_required
from blog.db import get_db

blueprint = Blueprint('blog', __name__)


@blueprint.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM article p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    if posts is not None:
        return render_template('blog/index.html', posts=posts)
    return render_template('home.html')


@blueprint.route('/home')
def home():
    return render_template('home.html')

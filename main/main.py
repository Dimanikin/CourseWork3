from flask import Blueprint, render_template, request

from utils.utils import load_post_by_user_name, search_for_posts, get_comments_by_post_id, get_post_by_pk, get_posts_all

main_bp = Blueprint('main', __name__)


@main_bp.get('/')
def index():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@main_bp.get('/posts/<int:postid>/')
def get_post(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", post=post, comments=comments)


@main_bp.get('/search/')
def search_post():
    posts = search_for_posts(request.args.get("word"))
    return render_template("search.html", posts=posts)


@main_bp.get('/user/<user_name>/')
def view_post_by_uer_name(user_name):
    posts = load_post_by_user_name(user_name)
    return render_template("user-feed.html", posts=posts)

from flask import Blueprint, jsonify

from logger import get_logger
from utils.utils import get_post_by_pk, get_posts_all

api_bp = Blueprint('api', __name__, url_prefix="/api/")

logger = get_logger(__name__)


@api_bp.route('posts/')
def api_posts():
    posts = get_posts_all()
    logger.info('api_posts')
    return jsonify(posts)


@api_bp.route('post/<int:postid>/')
def api_post(postid):
    post = get_post_by_pk(postid)
    logger.info('api_post')
    return jsonify(post)

from flask import Blueprint, request, jsonify
from models import db, User, Follow

api_bp = Blueprint('api', __name__)

@api_bp.route('/follow', methods=['POST'])
def follow_user():
    data = request.get_json()
    if not data or 'follower_id' not in data or 'followed_id' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid input'}), 400

    follower_id = data['follower_id']
    followed_id = data['followed_id']

    # Assuming you have appropriate checks and logic here
    new_follow = Follow(follower_id=follower_id, followed_id=followed_id)
    db.session.add(new_follow)
    db.session.commit()
    return jsonify({'message': 'User followed successfully'}), 200

@api_bp.route('/unfollow', methods=['POST'])
def unfollow_user():
    data = request.get_json()
    if not data or 'follower_id' not in data or 'followed_id' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid input'}), 400

    follower_id = data['follower_id']
    followed_id = data['followed_id']

    # Assuming you have appropriate checks and logic here
    follow = Follow.query.filter_by(follower_id=follower_id, followed_id=followed_id).first()
    if follow:
        db.session.delete(follow)
        db.session.commit()
        return jsonify({'message': 'User unfollowed successfully'}), 200
    else:
        return jsonify({'error': 'Not Found', 'message': 'Follow relationship does not exist'}), 404

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User, Profile, Favourite

api = Blueprint('api', __name__)

@api.route('/profiles', methods=['GET'])
@jwt_required()
def list_profiles():
    user_id = get_jwt_identity()
    profiles = Profile.query.filter(Profile.user_id_fk != user_id).all()
    return jsonify([p.to_dict() for p in profiles])

@api.route('/profiles', methods=['POST'])
@jwt_required()
def create_profile():
    data = request.get_json()
    user_id = get_jwt_identity()

    user_profiles = Profile.query.filter_by(user_id_fk=user_id).count()
    if user_profiles >= 3:
        return jsonify({'error': 'Max 3 profiles allowed'}), 400

    profile = Profile(user_id_fk=user_id, **data)
    db.session.add(profile)
    db.session.commit()
    return jsonify(profile.to_dict()), 201

@api.route('/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(profile.to_dict())

@api.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

@api.route('/profiles/<int:user_id>/favourite', methods=['POST'])
@jwt_required()
def favourite_user(user_id):
    current_user = get_jwt_identity()
    if current_user == user_id:
        return jsonify({'error': "Can't favourite yourself"}), 400

    existing = Favourite.query.filter_by(user_id_fk=current_user, fav_user_id_fk=user_id).first()
    if existing:
        return jsonify({'message': "Already favourited"}), 200

    fav = Favourite(user_id_fk=current_user, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify({'message': "User favourited"}), 201



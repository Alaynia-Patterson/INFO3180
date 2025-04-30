from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User, Profile, Favourite

api = Blueprint('api', __name__)

# GET all profiles except current user’s
@api.route('/profiles', methods=['GET'])
@jwt_required()
def list_profiles():
    user_id = get_jwt_identity()
    profiles = Profile.query.filter(Profile.user_id_fk != user_id).all()
    return jsonify([p.to_dict() for p in profiles]), 200


# POST a new profile for the logged-in user
@api.route('/profiles', methods=['POST'])
@jwt_required()
def create_profile():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()

        # Validate max 3 profiles
        existing_count = Profile.query.filter_by(user_id_fk=user_id).count()
        if existing_count >= 3:
            return jsonify({'error': 'Max 3 profiles allowed per user'}), 400

        # Create profile (fields must match your model)
        profile = Profile(
            user_id_fk=user_id,
            description=data.get('description'),
            parish=data.get('parish'),
            biography=data.get('biography'),
            sex=data.get('sex'),
            race=data.get('race'),
            birth_year=data.get('birth_year'),
            height=data.get('height'),
            fav_cuisine=data.get('fav_cuisine'),
            fav_colour=data.get('fav_colour'),
            fav_school_subject=data.get('fav_school_subject'),  # <- spelling must match your model!
            political=data.get('political'),
            religious=data.get('religious'),
            family_oriented=data.get('family_oriented')
        )

        db.session.add(profile)
        db.session.commit()
        return jsonify(profile.to_dict()), 201

    except Exception as e:
        print("DEBUG ERROR:", e)
        return jsonify({'error': 'Invalid request or missing data'}), 422


# GET single profile by ID
@api.route('/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(profile.to_dict()), 200

@api.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

# POST - Favourite another user
@api.route('/profiles/<int:user_id>/favourite', methods=['POST'])
@jwt_required()
def favourite_user(user_id):
    current_user = get_jwt_identity()

    if current_user == user_id:
        return jsonify({'error': "You cannot favourite yourself"}), 400

    # Check if already favourited
    existing = Favourite.query.filter_by(user_id_fk=current_user, fav_user_id_fk=user_id).first()
    if existing:
        return jsonify({'message': "User already favourited"}), 200

    fav = Favourite(user_id_fk=current_user, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()

    return jsonify({'message': "User favourited successfully"}), 201


@api.route('/search', methods=['GET'])
@jwt_required()
def search_profiles():
    try:
        query_args = request.args.to_dict()
        print(">>> Query Params:", query_args)

        return jsonify({
            "message": "Search route reached!",
            "params": query_args
        }), 200

    except Exception as e:
        print(">>> Search Error:", e)
        return jsonify({"error": str(e)}), 500


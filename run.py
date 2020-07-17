from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='admin').first():
            User.create_user(user='admin', email='admin@user.com', password='secret')
    except exc.IntegrityError:
            flask_app.run()
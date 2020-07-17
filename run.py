from app import create_app, db
from app.auth.models import User

if __name__=='__main__':
    flask_app = create_app('prod')
    with flask_app.app_context():
        db.create_all()
        # create default user (if not created)
        if not User.query.filter_by(user_name='default').first():
            User.create_user(user='default',
                             email='default@user.com',
                             password='Abcd!1234')
    flask_app.run()

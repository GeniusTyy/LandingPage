import click
from landpage.ext.database import db
from landpage.models import User


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()

def view_db():
    users = User.query.all()
    for user in users:
        print("-----------------------------------")
        print(f"Id: {user.id}\nEmail: {user.email}")


def populate_db():
    """Populate db with sample data"""
    data = [
        User(email="teste@gmail.com"),
        User(email="teste@teste.com"),
        User(email="teste@hotmail.com"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()



def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db, view_db]:
        app.cli.add_command(app.cli.command()(command))
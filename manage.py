
def deploy():
    """ Run Deployment Tasks """
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from models import User

    app = create_app()
    app.app_context().push()
    db.create_all()

    # migrate database to latest version
    init()
    stamp()
    migrate()
    upgrade()

deploy()

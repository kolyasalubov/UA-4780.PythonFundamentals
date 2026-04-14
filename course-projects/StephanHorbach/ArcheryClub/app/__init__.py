from pathlib import Path

from flask import Flask, render_template

from app.admin import admin_bp
from app.extensions import db
from app.public import public_bp
from app.seed import seed_database


def create_app(config_overrides=None, config_object="app.config.DemoConfig"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    if config_overrides:
        app.config.update(config_overrides)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    data_dir = app.config.get("DATA_DIR")
    if data_dir:
        Path(data_dir).mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        from app import models as app_models  # noqa: F401

        db.create_all()
        if app.config.get("AUTO_SEED_ON_STARTUP", True):
            seed_database()

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.cli.command("seed")
    def seed_command():
        seed_database()
        print("Database seeded.")

    return app

from pathlib import Path

from app import create_app
from app.models import Post, TrainingSlot


def test_create_app_uses_testing_config(tmp_path):
    app = create_app(
        {
            "TESTING": True,
            "AUTO_SEED_ON_STARTUP": False,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmp_path / 'test.db'}",
        }
    )

    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"].endswith("test.db")
    assert "sqlalchemy" in app.extensions
    assert app.config["AUTO_SEED_ON_STARTUP"] is False


def test_create_app_uses_project_instance_directory_by_default():
    app = create_app({"TESTING": True})
    expected_data_dir = Path(app.root_path).parent / "instance"

    assert Path(app.config["DATA_DIR"]) == expected_data_dir
    assert app.config["SQLALCHEMY_DATABASE_URI"] == (
        f"sqlite:///{expected_data_dir / 'archery_club.db'}"
    )


def test_create_app_skips_seed_when_auto_seed_disabled(tmp_path):
    app = create_app(
        {
            "TESTING": True,
            "AUTO_SEED_ON_STARTUP": False,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmp_path / 'test.db'}",
        }
    )

    with app.app_context():
        assert Post.query.count() == 0
        assert TrainingSlot.query.count() == 0

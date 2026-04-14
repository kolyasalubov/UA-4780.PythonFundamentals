from app.extensions import db
from app.models import Lead, Post, TrainingSlot
from app.seed import seed_database


def test_seed_database_creates_posts_and_slots_once(app):
    with app.app_context():
        db.create_all()

        seed_database()
        seed_database()

        assert Post.query.count() == 4
        assert TrainingSlot.query.count() == 3
        assert Lead.query.count() == 0

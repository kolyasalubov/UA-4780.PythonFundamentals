from app.extensions import db
from app.models import Post, TrainingSlot


POSTS = [
    {
        "title": "Why Alignment Decides the Shot Before the Draw",
        "slug": "alignment-before-draw",
        "excerpt": "A beginner-friendly explanation of stance, shoulder line, and repeatability.",
        "content": "Olympic recurve shooting begins long before the string moves. Stable feet, calm shoulders, and a consistent anchor create repeatable shots over an entire set.",
        "category": "Technique",
        "is_featured": True,
    },
    {
        "title": "What the 70-Meter Olympic Format Feels Like",
        "slug": "olympic-70m-format",
        "excerpt": "An introduction to sets, timing, and mental rhythm.",
        "content": "The Olympic round is not only about distance. It is about timing, emotional reset, and the discipline to repeat a familiar shot cycle under pressure.",
        "category": "Competition",
        "is_featured": True,
    },
    {
        "title": "Warm-Up Patterns That Protect the Archer",
        "slug": "warm-up-patterns-for-archers",
        "excerpt": "Mobility ideas for the upper back, shoulders, and focus before training.",
        "content": "A good warm-up prepares the shoulder girdle, opens the chest, and settles breathing so the first arrows do not feel rushed or heavy.",
        "category": "Preparation",
        "is_featured": False,
    },
    {
        "title": "How to Read Your First Olympic Recurve Setup",
        "slug": "first-olympic-recurve-setup",
        "excerpt": "A simple guide to riser, limbs, sight, and stabilizer choices.",
        "content": "Beginners do not need the most complex equipment. They need a balanced setup they can learn on with confidence and proper coaching.",
        "category": "Equipment",
        "is_featured": False,
    },
]

SLOTS = [
    {
        "title": "Beginner Starter Session",
        "day_label": "Monday",
        "start_time": "18:30",
        "level": "Beginner",
        "coach_name": "Iryna Melnyk",
        "capacity": 12,
        "description": "First contact with Olympic recurve basics, safety, and first scoring ends.",
        "is_featured": True,
    },
    {
        "title": "Olympic Technique Group",
        "day_label": "Wednesday",
        "start_time": "19:00",
        "level": "Beginner+",
        "coach_name": "Taras Koval",
        "capacity": 8,
        "description": "Posture, expansion, release, and rhythm for archers progressing toward regular training.",
        "is_featured": True,
    },
    {
        "title": "Club Saturday Practice",
        "day_label": "Saturday",
        "start_time": "10:00",
        "level": "Mixed",
        "coach_name": "Olha Danyliuk",
        "capacity": 14,
        "description": "An open club session with guided warm-up and a friendly scoring round.",
        "is_featured": False,
    },
]


def seed_database():
    if Post.query.count() == 0:
        for payload in POSTS:
            db.session.add(Post(**payload))

    if TrainingSlot.query.count() == 0:
        for payload in SLOTS:
            db.session.add(TrainingSlot(**payload))

    db.session.commit()

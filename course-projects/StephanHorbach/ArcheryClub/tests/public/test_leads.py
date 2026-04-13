from app.models import Lead


def test_signup_creates_new_lead(client, app):
    response = client.post(
        "/signup",
        data={
            "name": "Kateryna",
            "phone": "+380971112233",
            "email": "kateryna@example.com",
            "experience_level": "Beginner",
            "preferred_slot": "Beginner Starter Session",
            "message": "I want to try my first class this week.",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Your request has been sent" in response.data

    with app.app_context():
        lead = Lead.query.one()
        assert lead.name == "Kateryna"
        assert lead.status == "new"


def test_signup_requires_name_phone_and_message(client):
    response = client.post(
        "/signup",
        data={
            "name": "",
            "phone": "",
            "email": "kateryna@example.com",
            "experience_level": "Beginner",
            "preferred_slot": "Beginner Starter Session",
            "message": "",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Name, phone, and message are required." in response.data


def test_signup_rejects_malformed_optional_email(client, app):
    response = client.post(
        "/signup",
        data={
            "name": "Kateryna",
            "phone": "+380971112233",
            "email": "not-an-email",
            "experience_level": "Beginner",
            "preferred_slot": "Beginner Starter Session",
            "message": "I want to try my first class this week.",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Please provide a valid email address or leave the field empty." in response.data

    with app.app_context():
        assert Lead.query.count() == 0

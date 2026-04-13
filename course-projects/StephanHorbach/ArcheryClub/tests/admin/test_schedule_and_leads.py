from app.models import Lead, TrainingSlot


def test_admin_can_create_edit_and_delete_schedule_slot(client, app):
    create_response = client.post(
        "/admin/schedule/new",
        data={
            "title": "Sunday Mobility Session",
            "day_label": "Sunday",
            "start_time": "11:00",
            "level": "Beginner",
            "coach_name": "Sofiia Bondar",
            "capacity": "10",
            "description": "A light technical reset before the week starts.",
            "is_featured": "on",
        },
        follow_redirects=True,
    )
    assert create_response.status_code == 200

    with app.app_context():
        slot = TrainingSlot.query.filter_by(title="Sunday Mobility Session").first()
        assert slot is not None
        slot_id = slot.id

    edit_response = client.post(
        f"/admin/schedule/{slot_id}/edit",
        data={
            "title": "Sunday Mobility Session Updated",
            "day_label": "Sunday",
            "start_time": "11:30",
            "level": "Beginner",
            "coach_name": "Sofiia Bondar",
            "capacity": "10",
            "description": "Updated schedule copy.",
            "is_featured": "",
        },
        follow_redirects=True,
    )
    assert edit_response.status_code == 200

    delete_response = client.post(f"/admin/schedule/{slot_id}/delete", follow_redirects=True)
    assert delete_response.status_code == 200

    with app.app_context():
        assert TrainingSlot.query.filter_by(title="Sunday Mobility Session Updated").first() is None



def test_admin_can_update_lead_status(client, app):
    with app.app_context():
        lead = Lead(
            name="Nazar",
            phone="+380991112233",
            email="nazar@example.com",
            experience_level="Beginner",
            preferred_slot="Beginner Starter Session",
            message="Please contact me after work.",
        )
        from app.extensions import db

        db.session.add(lead)
        db.session.commit()
        lead_id = lead.id

    response = client.post(
        f"/admin/leads/{lead_id}/status",
        data={"status": "booked"},
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app.app_context():
        from app.extensions import db

        assert db.session.get(Lead, lead_id).status == "booked"



def test_admin_rejects_invalid_schedule_capacity(client, app):
    response = client.post(
        "/admin/schedule/new",
        data={
            "title": "Broken Capacity Session",
            "day_label": "Sunday",
            "start_time": "11:00",
            "level": "Beginner",
            "coach_name": "Sofiia Bondar",
            "capacity": "zero",
            "description": "This should not be saved.",
            "is_featured": "on",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Capacity must be a positive whole number." in response.data

    with app.app_context():
        assert TrainingSlot.query.filter_by(title="Broken Capacity Session").first() is None



def test_admin_rejects_invalid_lead_status(client, app):
    with app.app_context():
        lead = Lead(
            name="Nazar",
            phone="+380991112233",
            email="nazar@example.com",
            experience_level="Beginner",
            preferred_slot="Beginner Starter Session",
            message="Please contact me after work.",
        )
        from app.extensions import db

        db.session.add(lead)
        db.session.commit()
        lead_id = lead.id

    response = client.post(
        f"/admin/leads/{lead_id}/status",
        data={"status": "archived"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Invalid lead status." in response.data

    with app.app_context():
        from app.extensions import db

        assert db.session.get(Lead, lead_id).status == "new"

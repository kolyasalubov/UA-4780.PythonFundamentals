import pytest
from flask import render_template_string

from app.extensions import db
from app.seed import seed_database


def test_home_page_loads_with_key_sections(client, app):
    with app.app_context():
        db.create_all()
        seed_database()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Archery Society Kyiv" in response.data
    assert b"Trial Training" in response.data
    assert b"How the first session works" in response.data
    assert b'class="site-header"' in response.data
    assert b'class="hero"' in response.data
    assert b'href="/"' in response.data
    assert b'href="/trainings"' in response.data
    assert b'href="/contacts"' in response.data
    assert b'href="/blog"' in response.data
    assert b'href="/admin"' in response.data
    assert b"Warm-Up Patterns That Protect the Archer" not in response.data
    assert b"Club Saturday Practice" not in response.data


def test_trainings_page_loads_with_slot_details(client, app):
    with app.app_context():
        db.create_all()
        seed_database()

    response = client.get("/trainings")

    assert response.status_code == 200
    assert b"Beginner Starter Session" in response.data
    assert b"Iryna Melnyk" in response.data


def test_contacts_page_loads_with_contact_details(client):
    response = client.get("/contacts")

    assert response.status_code == 200
    assert b"hello@archerykyiv.example" in response.data
    assert b"Kyiv, Ukraine" in response.data


def test_nav_helper_raises_for_missing_required_endpoint(app):
    with app.test_request_context("/"):
        with pytest.raises(RuntimeError, match="public.missing"):
            render_template_string('{{ nav_href("public.missing") }}')

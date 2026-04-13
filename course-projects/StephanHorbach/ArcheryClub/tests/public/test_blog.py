from app.extensions import db
from app.seed import seed_database


def test_blog_list_and_post_detail_render(client, app):
    with app.app_context():
        db.create_all()
        seed_database()

    blog_response = client.get("/blog")
    detail_response = client.get("/blog/alignment-before-draw")

    assert blog_response.status_code == 200
    assert b"Why Alignment Decides the Shot Before the Draw" in blog_response.data
    assert detail_response.status_code == 200
    assert b"Stable feet" in detail_response.data


def test_unknown_slug_returns_custom_404(client):
    response = client.get("/blog/does-not-exist")
    assert response.status_code == 404
    assert b"Page not found" in response.data

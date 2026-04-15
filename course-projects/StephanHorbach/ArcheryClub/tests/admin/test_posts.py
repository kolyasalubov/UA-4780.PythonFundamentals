from app.extensions import db
from app.models import Post
from app.seed import seed_database


def test_admin_dashboard_and_posts_list_load(client, app):
    with app.app_context():
        db.create_all()
        seed_database()

    assert client.get("/admin").status_code == 200
    response = client.get("/admin/posts")
    assert response.status_code == 200
    assert b"Manage Posts" in response.data



def test_admin_can_create_edit_and_delete_post(client, app):
    create_response = client.post(
        "/admin/posts/new",
        data={
            "title": "Club Focus Drill",
            "slug": "club-focus-drill",
            "category": "Technique",
            "excerpt": "A short drill for calm shot timing.",
            "content": "Use a fixed pre-shot rhythm and reset after each arrow.",
            "is_featured": "on",
        },
        follow_redirects=True,
    )
    assert create_response.status_code == 200

    with app.app_context():
        post = Post.query.filter_by(slug="club-focus-drill").first()
        assert post is not None
        post_id = post.id

    edit_response = client.post(
        f"/admin/posts/{post_id}/edit",
        data={
            "title": "Club Focus Drill Updated",
            "slug": "club-focus-drill",
            "category": "Technique",
            "excerpt": "A short drill for calm shot timing.",
            "content": "Updated content.",
            "is_featured": "",
        },
        follow_redirects=True,
    )
    assert edit_response.status_code == 200

    delete_response = client.post(f"/admin/posts/{post_id}/delete", follow_redirects=True)
    assert delete_response.status_code == 200

    with app.app_context():
        assert Post.query.filter_by(slug="club-focus-drill").first() is None



def test_admin_rejects_duplicate_post_slug(client, app):
    with app.app_context():
        db.create_all()
        seed_database()

    response = client.post(
        "/admin/posts/new",
        data={
            "title": "Duplicate Slug Post",
            "slug": "alignment-before-draw",
            "category": "Technique",
            "excerpt": "Trying to reuse an existing slug.",
            "content": "This should be rejected.",
            "is_featured": "on",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"A post with this slug already exists." in response.data

    with app.app_context():
        assert Post.query.filter_by(title="Duplicate Slug Post").first() is None

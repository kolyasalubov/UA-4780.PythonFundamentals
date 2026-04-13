import re

from flask import abort, flash, redirect, render_template, request, url_for

from app.extensions import db
from app.models import Lead
from app.models import Post, TrainingSlot
from app.public import public_bp

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _is_valid_email(email):
    return bool(EMAIL_PATTERN.fullmatch(email))


@public_bp.get("/")
def home():
    featured_posts = (
        Post.query.filter_by(is_featured=True)
        .order_by(Post.created_at.desc())
        .limit(3)
        .all()
    )
    featured_slots = (
        TrainingSlot.query.filter_by(is_featured=True)
        .order_by(TrainingSlot.id.asc())
        .limit(3)
        .all()
    )
    return render_template(
        "public/home.html",
        featured_posts=featured_posts,
        featured_slots=featured_slots,
    )


@public_bp.get("/trainings")
def trainings():
    slots = TrainingSlot.query.order_by(TrainingSlot.id.asc()).all()
    return render_template("public/trainings.html", slots=slots)


@public_bp.get("/blog")
def blog():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("public/blog.html", posts=posts)


@public_bp.get("/blog/<slug>")
def post_detail(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post is None:
        abort(404)
    return render_template("public/post_detail.html", post=post)


@public_bp.post("/signup")
def signup():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    experience_level = request.form.get("experience_level", "Beginner").strip()
    preferred_slot = request.form.get("preferred_slot", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not phone or not message:
        flash("Name, phone, and message are required.", "error")
        return redirect(url_for("public.home"))

    if email and not _is_valid_email(email):
        flash("Please provide a valid email address or leave the field empty.", "error")
        return redirect(url_for("public.home"))

    db.session.add(
        Lead(
            name=name,
            phone=phone,
            email=email,
            experience_level=experience_level,
            preferred_slot=preferred_slot,
            message=message,
        )
    )
    db.session.commit()

    flash("Your request has been sent. We will contact you shortly.", "success")
    return redirect(url_for("public.home"))


@public_bp.get("/contacts")
def contacts():
    return render_template("public/contacts.html")

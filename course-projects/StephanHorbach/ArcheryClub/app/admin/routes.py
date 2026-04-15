from types import SimpleNamespace

from flask import abort, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

from app.admin import admin_bp
from app.extensions import db
from app.models import Lead, Post, TrainingSlot

VALID_LEAD_STATUSES = {"new", "contacted", "booked"}


def _clean_post_form():
    return {
        "title": request.form.get("title", "").strip(),
        "slug": request.form.get("slug", "").strip(),
        "category": request.form.get("category", "").strip(),
        "excerpt": request.form.get("excerpt", "").strip(),
        "content": request.form.get("content", "").strip(),
        "is_featured": request.form.get("is_featured") == "on",
    }


def _post_form_view(form_data):
    return SimpleNamespace(**form_data)


def _validate_post_form(form_data):
    errors = []
    for field_name, label in (
        ("title", "Title"),
        ("slug", "Slug"),
        ("category", "Category"),
        ("excerpt", "Excerpt"),
        ("content", "Content"),
    ):
        if not form_data[field_name]:
            errors.append(f"{label} is required.")
    return errors


def _clean_schedule_form():
    return {
        "title": request.form.get("title", "").strip(),
        "day_label": request.form.get("day_label", "").strip(),
        "start_time": request.form.get("start_time", "").strip(),
        "level": request.form.get("level", "").strip(),
        "coach_name": request.form.get("coach_name", "").strip(),
        "capacity": request.form.get("capacity", "").strip(),
        "description": request.form.get("description", "").strip(),
        "is_featured": request.form.get("is_featured") == "on",
    }


def _schedule_form_view(form_data):
    return SimpleNamespace(**form_data)


def _parse_capacity(raw_capacity):
    try:
        capacity = int(raw_capacity)
    except (TypeError, ValueError):
        return None
    if capacity <= 0:
        return None
    return capacity


def _validate_schedule_form(form_data):
    errors = []
    for field_name, label in (
        ("title", "Title"),
        ("day_label", "Day"),
        ("start_time", "Start time"),
        ("level", "Level"),
        ("coach_name", "Coach"),
        ("description", "Description"),
    ):
        if not form_data[field_name]:
            errors.append(f"{label} is required.")

    if _parse_capacity(form_data["capacity"]) is None:
        errors.append("Capacity must be a positive whole number.")

    return errors


def _flash_errors(errors):
    for message in errors:
        flash(message, "error")


def _commit_with_duplicate_slug_guard():
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("A post with this slug already exists.", "error")
        return False
    return True


@admin_bp.get("")
@admin_bp.get("/")
def dashboard():
    return render_template(
        "admin/dashboard.html",
        post_count=Post.query.count(),
        slot_count=TrainingSlot.query.count(),
        lead_count=Lead.query.count(),
    )


@admin_bp.get("/posts")
def posts_list():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("admin/posts_list.html", posts=posts)


@admin_bp.route("/posts/new", methods=["GET", "POST"])
def posts_new():
    if request.method == "POST":
        form_data = _clean_post_form()
        errors = _validate_post_form(form_data)
        if errors:
            _flash_errors(errors)
            return render_template("admin/post_form.html", post=_post_form_view(form_data))

        post = Post(**form_data)
        db.session.add(post)
        if not _commit_with_duplicate_slug_guard():
            return render_template("admin/post_form.html", post=_post_form_view(form_data))
        flash("Post created.", "success")
        return redirect(url_for("admin.posts_list"))

    return render_template("admin/post_form.html", post=None)


@admin_bp.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def posts_edit(post_id):
    post = db.session.get(Post, post_id)
    if post is None:
        abort(404)

    if request.method == "POST":
        form_data = _clean_post_form()
        errors = _validate_post_form(form_data)
        if errors:
            _flash_errors(errors)
            return render_template("admin/post_form.html", post=_post_form_view(form_data))

        post.title = form_data["title"]
        post.slug = form_data["slug"]
        post.category = form_data["category"]
        post.excerpt = form_data["excerpt"]
        post.content = form_data["content"]
        post.is_featured = form_data["is_featured"]
        if not _commit_with_duplicate_slug_guard():
            return render_template("admin/post_form.html", post=_post_form_view(form_data))
        flash("Post updated.", "success")
        return redirect(url_for("admin.posts_list"))

    return render_template("admin/post_form.html", post=post)


@admin_bp.post("/posts/<int:post_id>/delete")
def posts_delete(post_id):
    post = db.session.get(Post, post_id)
    if post is None:
        abort(404)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("admin.posts_list"))


@admin_bp.get("/schedule")
def schedule_list():
    slots = TrainingSlot.query.order_by(TrainingSlot.id.asc()).all()
    return render_template("admin/schedule_list.html", slots=slots)


@admin_bp.route("/schedule/new", methods=["GET", "POST"])
def schedule_new():
    if request.method == "POST":
        form_data = _clean_schedule_form()
        errors = _validate_schedule_form(form_data)
        if errors:
            _flash_errors(errors)
            return render_template(
                "admin/schedule_form.html",
                slot=_schedule_form_view(form_data),
            )

        slot = TrainingSlot(
            title=form_data["title"],
            day_label=form_data["day_label"],
            start_time=form_data["start_time"],
            level=form_data["level"],
            coach_name=form_data["coach_name"],
            capacity=_parse_capacity(form_data["capacity"]),
            description=form_data["description"],
            is_featured=form_data["is_featured"],
        )
        db.session.add(slot)
        db.session.commit()
        flash("Schedule entry created.", "success")
        return redirect(url_for("admin.schedule_list"))

    return render_template("admin/schedule_form.html", slot=None)


@admin_bp.route("/schedule/<int:slot_id>/edit", methods=["GET", "POST"])
def schedule_edit(slot_id):
    slot = db.session.get(TrainingSlot, slot_id)
    if slot is None:
        abort(404)

    if request.method == "POST":
        form_data = _clean_schedule_form()
        errors = _validate_schedule_form(form_data)
        if errors:
            _flash_errors(errors)
            return render_template(
                "admin/schedule_form.html",
                slot=_schedule_form_view(form_data),
            )

        slot.title = form_data["title"]
        slot.day_label = form_data["day_label"]
        slot.start_time = form_data["start_time"]
        slot.level = form_data["level"]
        slot.coach_name = form_data["coach_name"]
        slot.capacity = _parse_capacity(form_data["capacity"])
        slot.description = form_data["description"]
        slot.is_featured = form_data["is_featured"]
        db.session.commit()
        flash("Schedule entry updated.", "success")
        return redirect(url_for("admin.schedule_list"))

    return render_template("admin/schedule_form.html", slot=slot)


@admin_bp.post("/schedule/<int:slot_id>/delete")
def schedule_delete(slot_id):
    slot = db.session.get(TrainingSlot, slot_id)
    if slot is None:
        abort(404)
    db.session.delete(slot)
    db.session.commit()
    flash("Schedule entry deleted.", "success")
    return redirect(url_for("admin.schedule_list"))


@admin_bp.get("/leads")
def leads_list():
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return render_template("admin/leads_list.html", leads=leads)


@admin_bp.post("/leads/<int:lead_id>/status")
def leads_status(lead_id):
    lead = db.session.get(Lead, lead_id)
    if lead is None:
        abort(404)
    status = request.form.get("status", "").strip()
    if status not in VALID_LEAD_STATUSES:
        flash("Invalid lead status.", "error")
        return redirect(url_for("admin.leads_list"))
    lead.status = status
    db.session.commit()
    flash("Lead status updated.", "success")
    return redirect(url_for("admin.leads_list"))

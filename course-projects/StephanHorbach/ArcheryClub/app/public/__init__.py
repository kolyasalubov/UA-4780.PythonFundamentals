from flask import Blueprint, current_app, url_for

public_bp = Blueprint("public", __name__)


@public_bp.app_template_global()
def nav_href(endpoint=None, fallback=None, **values):
    if endpoint and endpoint in current_app.view_functions:
        return url_for(endpoint, **values)
    if fallback is not None:
        return fallback
    if endpoint:
        raise RuntimeError(f"Endpoint '{endpoint}' is not registered.")
    return "#"


from app.public import routes  # noqa: E402,F401

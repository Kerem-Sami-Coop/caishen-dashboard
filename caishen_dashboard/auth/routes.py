# import uuid
# from flask import redirect, url_for, render_template, flash, current_app, request, session
# from flask_login import login_user, logout_user, current_user, login_required
# from caishen_dashboard import db
# from caishen_dashboard.auth import bp
# # from caishen_dashboard.auth import _build_auth_url, _build_msal_app
# from caishen_dashboard.auth.models import User


# @bp.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(  # Also logout from your tenant"s web session
#         current_app.config["AUTHORITY"] + "/oauth2/v2.0/logout" + "?post_logout_redirect_uri=" + \
#         url_for("main.index", _external=True)
#     )


# @bp.route("/login", methods=["GET"])
# def login():
#     next_url = request.args.get("next")
#     if not current_user.is_anonymous:
#         flash(f"Logged in as {current_user.name}", "success")
#         return redirect(next_url or url_for("main.index"))
#     else:
#         session["state"] = str(uuid.uuid4())
#         auth_url = _build_auth_url(scopes=current_app.config["SCOPE"], state=session["state"])
#         return render_template("auth/login.html", auth_url=auth_url)


# @bp.route(current_app.config["REDIRECT_PATH"], methods=["GET"])
# def authorized():
#     next_url = request.args.get("next")

#     if request.args.get("state") != session.get("state"):
#         return redirect(url_for("main.index"))  # No-OP. Goes back to Index page

#     if not current_user.is_anonymous:
#         return redirect(next_url or url_for("main.index"))

#     if request.args.get("code"):
#         result = _build_msal_app().acquire_token_by_authorization_code(
#             request.args["code"],
#             scopes=current_app.config["SCOPE"],  # Misspelled scope would cause an HTTP 400 error here
#             redirect_uri=url_for("auth.authorized", _external=True))
#         if "error" in result:
#             flash("Authentication failed", "danger")
#             return redirect(url_for("auth.login"))

#         claims = result.get("id_token_claims")
#         name = claims["name"]
#         email = claims["preferred_username"]
#         if name is None:
#             flash("Authentication failed.")
#             return redirect(url_for("auth.login"))
#         user = User.query.filter_by(name=name).first()

#         if not user:
#             user = User(name=name, email=email)
#             db.session.add(user)
#             db.session.commit()

#         logged_in = login_user(user, remember=True, force=True)

#     else:
#         redirect(url_for("auth.login"))

#     return redirect(next_url or url_for("main.index"))
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

from caishen_dashboard.auth.utils import login_required
from caishen_dashboard import db
from caishen_dashboard.auth.forms import LoginForm
from caishen_dashboard.auth.forms import RegistrationForm
from caishen_dashboard.auth.models import User
from caishen_dashboard.auth import bp


@bp.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("server.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            error = "Invalid username or password"
            return render_template("auth/login.html", form=form, error=error)

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("server.index")
        return redirect(next_page)

    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@bp.route("/register/", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("server/index.html"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", title="Register", form=form)

from flask import Blueprint, render_template, abort

auth_bp = Blueprint('simple_page', __name__,
                        template_folder='templates/authentication')

@auth_bp.route('/login')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        abort(500, description=str(e))

@auth_bp.route('/auth')
def auth():
    return "Authentication Page"


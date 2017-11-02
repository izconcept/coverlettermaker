from flask import render_template, Blueprint

website_blueprint = Blueprint('website_blueprint', __name__)


@website_blueprint.route('/')
def index():
    return render_template('index.html')


@website_blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@website_blueprint.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


from project.routes.api import *

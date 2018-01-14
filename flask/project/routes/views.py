from flask import render_template, Blueprint, session, request, redirect
import requests
import json

website_blueprint = Blueprint('website_blueprint', __name__)


@website_blueprint.route('/')
def index():
    tags = []
    if 'tags' in session:
        tags = session['tags']
    if 'code' in request.args:
        code = request.args['code']
        r = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data={'grant_type': 'authorization_code',
                                                                                 'code': code,
                                                                                 'redirect_uri': 'http://localhost/',
                                                                                 'client_id': '78rpczh5d7fm7p',
                                                                                 'client_secret': 'rhWRnE3BnmN0Ou3l'})
        session['token'] = json.loads(r.text)["access_token"]
        r = requests.get("https://api.linkedin.com/v1/people/~?format=json", headers={'Authorization': "Bearer " + session['token']})
        profile = json.loads(r.text)
        session['user_name'] = profile['firstName'] + " " + profile['lastName']


        return render_template('index.html', tags=tags, name=session['user_name'])
    else:
        return redirect('/login')


@website_blueprint.route('/login')
def login():
    return render_template('login.html')


@website_blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@website_blueprint.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500

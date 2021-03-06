import urllib.request
from flask import redirect, request, Blueprint, make_response, flash, session, url_for
from werkzeug.utils import secure_filename

from project import logger
from project.services.html_parser import *
from project.services.pdf_maker import *
from project.services.pdf_parser import *


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/v0.0/addtag', methods=['GET'])
def add_tag():
    if request.args.get('tag'):
        if 'tags' in session:
            tags = session['tags']
            tags.append(request.args.get('tag'))
            session['tags'] = tags
        else:
            session['tags'] = [request.args.get('tag')]
        return request.args.get('tag')
    else:
        return 'Failure'


@api_blueprint.route('/api/v0.0/removeTag', methods=['GET'])
def remove_tag():
    if request.args.get('tag'):
        print(request.args.get('tag'))
        if 'tags' in session:
            tags = session['tags']
            new_tags = [tag for tag in tags if tag != request.args.get('tag')]
            session['tags'] = new_tags
            return 'Success'
        else:
            return 'Failure'
    else:
        return 'Failure'


@api_blueprint.route('/api/v0.0/createcover', methods=['GET'])
def create_cover():
    if request.args.get('url'):
        try:

            req = urllib.request.urlopen(request.args.get('url'))
            res_bytes = req.read()
            resp_string = res_bytes.decode("utf8")

            items = html_parser(resp_string)
            items = match_tags(items)
            pdf_out = gen_pdf(items)

            resp = make_response(pdf_out)
            resp.headers['Content-Disposition'] = "attachment; filename='test.pdf"
            resp.mimetype = 'application/pdf'

            # return redirect('/')
            return resp

        except ValueError:
            print("bad URL", flush=True)
            flash("incorrect URL")

        except Exception:
            print(Exception, flush=True)
            flash("Server error occured")
    else:
        print('Missing URL', flush=True)
        if not request.args.get('url'):
            return "Missing URL argument"
        else:
            return "Bad Request"


@api_blueprint.route('/api/v0.0/uploadcv', methods=['POST'])
def upload_cv():
    if request.method == 'POST':
        if 'cv' not in request.files:
            flash('No file found')
            return redirect(request.url)
        else:
            cv = request.files['cv']
            if cv.filename == '':
                return redirect(request.url)
            from io import BytesIO
            parse_cv(BytesIO(cv.read()))
    return "file received"

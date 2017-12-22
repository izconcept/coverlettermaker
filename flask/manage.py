from project import create_app, logger, db
from flask_script import Manager
import coverage
import unittest

logger.info('Server has started.')

# Defines which parts of the code to include and omit when calculating code coverage.
COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'tests/*',
        'project/routes/*'
    ]
)
COV.start()

# Creates the Flask application object that we use to initialize things in the app.
app = create_app()

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


import project.models
db.create_all(app=app)

# Initializes the Manager object, which allows us to run terminal commands on the
# Flask application while it's running.
manager = Manager(app)


# While the application is running, you can run the following command in a new terminal:
# 'docker-compose run --rm flask python manage.py cov' to run all the tests in the
# 'tests' directory. If all the tests pass, it will generate a coverage report.
@manager.command
def cov():
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    else:
        return 1


# Enter 'docker-compose run --rm flask python manage.py test' to run all the
# tests in the 'tests' directory, but provides no coverage report.
@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


# Enter 'docker-compose run --rm flask python manage.py test_one NAME_OF_FILE' to run only one
# test file in the 'tests' directory. It provides no coverage report.
#
# Example: 'docker-compose run --rm flask python manage.py test_one test_website'
# Note that you do not need to put the extension of the test file.
@manager.command
def test_one(test_file):
    tests = unittest.TestLoader().discover('tests', pattern=test_file + '.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

# Starts the Flask app.
if __name__ == '__main__':
    manager.run()


#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################
from typing import List, Any
from bottle import route, run, default_app, debug, static_file, template, request
from hashlib import sha256
from repl_comments import create_hash, correct_password


def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page




def index():
    return htmlify("My lovely website",
                   "This is going to be an awesome website, when it is finished.")
route('/', 'GET', index)

def static_file_callback(filename):
    return static_file(filename, root='static')

route('/static/<filename>', 'GET', static_file_callback)

@route('/login')

def login_page():
    return '''
        <h1>Welcome</h1>
        <h3>You have to login first to add comments.</h3>
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')

def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<h1>Welcome {}!</h1>" \
               "<h2>Your login information was correct.</h2>".format(username)
    else:
        return "<h1>Login failed.</h1>"

def check_login(username, password):
    input_password = create_hash(password)
    if input_password == correct_password:
        return True
    else:
        return False







#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()


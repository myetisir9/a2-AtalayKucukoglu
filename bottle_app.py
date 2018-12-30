
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################
import codecs
from bottle import *
from hashlib import sha256

## retrived from
# https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

## password: simplicity
correct_password = "2ae0514924b1db04e8c45002326641b5e6c74f182288ae8702d5c7250374669e"
comments = []
logged_in = False

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

def static_file_callback(filename):
    return static_file(filename, root='static')

route('/static/<filename>', 'GET', static_file_callback)

@route('/')

def login_page():
    return template('./static/index.html')

@route('/login', method='POST')

def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<h1>Welcome {}!</h1>" \
               "<h2>Your login information was correct.</h2>".format(username)
    else:
        return '''
        <h1>Login Failed</h1>
        <button onclick="location.href='{}'">Try Again</button>

    '''

def check_login(username, password):
    input_password = create_hash(password)
    if input_password == correct_password:
        logged_in = True
        return True
    else:
        return False

def add_comments():
    i = 0
    while True:
        print("Enter comment (or exit with -1): ")
        comment = input()
        if comment == "-1":
            print("Exitted succesfully")
            break
        else:
            comments.append(comment)
            print("Comments:")
            for i in range(len(comments)):
                print(str(i + 1) + ". " + comments[i])

            i += 1



#route to css stylesheet

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

# route to the pages

@route('/index.html')
def index():
    return template('./static/index.html')

@route('/syrup.html')
def syrup():
    return template('./static/syrup.html')

@route('/milk.html')
def milk():
    return template('./static/milk.html')

@route('/baklava.html')
def baklava():
    return template('./static/baklava.html')

@route('/kunefe.html')
def kunefe():
    return template('./static/kunefe.html')

@route('/kadayif.html')
def kadayif():
    return template('./static/kadayif.html')

@route('/keskul.html')
def keskul():
    return template('./static/keskul.html')

@route('/sutlac.html')
def sutlac():
    return template('./static/sutlac.html')

@route('/kazandibi.html')
def kazandibi():
    return template('./static/kazandibi.html')







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


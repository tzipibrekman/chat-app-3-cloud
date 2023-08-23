from flask import Flask, render_template, request
server = Flask(__name__)

def handling_request_register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return f"data from user: Name - {name}, password - {password}"
    return render_template('register.html')


def handling_request_login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return f"data from user: Name - {name}, password - {password}"
    return render_template('login.html')


def handling_request_lobby():
    if request.method == 'POST':
        room=request.form['new_room']
    return render_template('lobby.html')


@server.route('/', methods=['GET', 'POST'])
def homePage():
    return handling_request_register()

@server.route('/register', methods=['GET', 'POST'])
def register():
    return handling_request_register()

@server.route('/login', methods=['GET', 'POST'])
def login():
    return handling_request_login()

@server.route('/lobby', methods=['GET', 'POST'])
def lobby():
    return handling_request_lobby()


if __name__ == "__main__":
 server.run(host='0.0.0.0',debug=True)
























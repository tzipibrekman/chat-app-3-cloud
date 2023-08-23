from flask import Flask, render_template
server = Flask(__name__)
@server.route("/")
def homePage():
 return render_template('register.html')
if __name__ == "__main__":
 server.run(host='0.0.0.0')
from flask import Flask, render_template, request,redirect,session
import os
from datetime import date, datetime
import csv
import base64
server = Flask(__name__)
server.secret_key = "123123"


def encode_password(user_pass):
    pass_bytes = user_pass.encode('ascii')
    base64_bytes = base64.b64encode(pass_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decode_password(user_pass):
    base64_bytes = user_pass.encode('ascii')
    pass_bytes = base64.b64decode(base64_bytes)
    user_pass = pass_bytes.decode('ascii')
    return user_pass


def check_user_existing(name,password):
    with open('users.csv', 'r') as myFile:
     myReader = csv.reader(myFile)
     users=list(myReader)
    encode_pass=encode_password(password)
    for user in users:
        if user[0]==name and decode_password(user[1])==password:
           return True
    return False    

def handling_request_register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        encoded_pass=encode_password(password)
        #בדוק אם כבר קיים
        if check_user_existing(name,password):
            return redirect('/login')
        else:
            with open('users.csv','a',newline='')as file:
                writer=csv.writer(file)
                writer.writerow([name,encoded_pass])
            return redirect('/lobby')
    return render_template('register.html')
    


def handling_request_login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if check_user_existing(name,password):
            session['username'] = name
            return redirect('/lobby')
        else:
            return "invalid"
    return render_template('login.html')

def handling_request_lobby():
    if 'username' in session:
       if request.method == 'POST':
           room=request.form['new_room']
           with open('rooms/' + room + ".txt", 'w') as f:
               f.write("")
       rooms = os.listdir('rooms/') 
       new_rooms = [x[:-4] for x in rooms]
       return render_template('lobby.html',room_names=new_rooms)
    else:
        return redirect('/login')


def handling_request_chat(room_name):
    user_name=session['username']
    if request.method == 'POST':
        print ({room_name})
        message=request.form['msg']
        file_path = "rooms/{}.txt".format(room_name)
        with open('rooms/' + room_name+ ".txt", 'a',newline="") as f:
          f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+", "+user_name +" : " +"\n"+ message +"\n")
   
    with open('rooms/' + room_name+ ".txt", 'r') as file:
        file.seek(0)
        all_data = file.read()
        return all_data
  

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

@server.route('/chat/<room_name>', methods=['GET', 'POST'])
def chat(room_name):
     return render_template('chat.html',room=room_name)

@server.route('/api/chat/<room_name>', methods=['GET', 'POST'])
def api_chat(room_name):
    return handling_request_chat(room_name)

@server.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return handling_request_login()


if __name__ == "__main__":
 server.run(host='0.0.0.0',debug=True)


from flask import Flask, render_template, request,redirect,session
import os
import csv
server = Flask(__name__)
app = Flask(__name__)
app.secret_key = "123123"

def check_user_existing(name,password):
    with open('../users.csv', 'r') as myFile:
     myReader = csv.reader(myFile)
     users=list(myReader)
    if [name,password] in users:
           return True
    return False    

def handling_request_register():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        #בדוק אם כבר קיים
        if check_user_existing(name,password):
            return redirect('/login')
        else:
            with open('../users.csv','a',newline='')as file:
                writer=csv.writer(file)
                writer.writerow([name,password])
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
               f.write(room)
       rooms = os.listdir('rooms/') 
       new_rooms = [x[:-4] for x in rooms]
       return render_template('lobby.html',room_names=new_rooms)
    else:
        return redirect('/login')



def handling_request_chat(room_name):
    
    return render_template('chat.html',room=room_name)


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
    return handling_request_chat(room_name)

@server.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return handling_request_login()


if __name__ == "__main__":
 server.run(host='0.0.0.0',debug=True)
























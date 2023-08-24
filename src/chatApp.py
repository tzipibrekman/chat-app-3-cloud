from flask import Flask, render_template, request
server = Flask(__name__)

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
            return redirect('/lobby')
    return render_template('login.html')


@server.route('/', methods=['GET', 'POST'])
def homePage():
         return handling_request_register()

@server.route('/register', methods=['GET', 'POST'])
def register():
    return handling_request_register()

@server.route('/login', methods=['GET', 'POST'])
def login():
    return handling_request_login()



if __name__ == "__main__":
 server.run(host='0.0.0.0',debug=True)
























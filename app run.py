from flask import Flask, request, render_template,session,redirect,url_for
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBbXawfxVGrNrqYCfALIRdBmXTKcDObMsg",
  'authDomain': "python-60020.firebaseapp.com",
  'projectId': "python-60020",
  'storageBucket': "python-60020.appspot.com",
  'messagingSenderId': "425689112125",
  'appId': "1:425689112125:web:b9793fedd9d0563b571454",
  'measurementId': "G-2NP88WT5YX",
  'databaseURL':''
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
       email = request.form.get("email")
       password = request.form.get("pass")
       
       try:
           user = auth.sign_in_with_email_and_password(email, password)
           session['email'] = email
           return redirect(url_for('principal'))
       except:
          # flash('Dados incorretos!')
           print("dados incorretos")
           
    return render_template('index.html')


@app.route("/create_account", methods=['GET', 'POST'])
def create_account():
    if request.method == "POST":
       email = request.form.get("email")
       password = request.form.get("pass")

       result = auth.create_user_with_email_and_password(email, password)

       if type(result) == type({}):
           session['email'] = email
           return redirect(url_for('principal'))

    return render_template('create_account.html')

@app.route("/principal", methods=['GET', 'POST'])
def principal():
    email = session['email']
    print(email)
    return render_template('principal.html') 

if __name__ == '__main__':
    app.run(debug=True)
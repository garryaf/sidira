from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime


@app.route('/')
def login():
    return render_template("login.html")

##@app.route('/')
#def index():
#   pageData = {
#        "breadcrumb": "Dashboard",
#        "pageHeader": "Dashboard",
#        "pages": "dashboard.html"
#    }
#    return render_template("index.html", pageData=pageData)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        retype_password = request.form['retype_password']

        if password != retype_password:
            error = 'Password tidak cocok!'
            return render_template('register.html', error=error)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO user_t (nama, username, email, password) VALUES (%s, %s)"
        values = (nama, username, email, password)
        mysql.connection.commit()
        cur.close()
      
          

        return redirect(url_for('success'))


    return render_template('register.html')


@app.route('/success')
def success():
    return 'Registration Successful!'


if __name__ == '__main__':
    app.run(debug=True)


@app.errorhandler(404)
def notfound(error):
    return render_template("404.html")
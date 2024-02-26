from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = "users.db"

@app.route("/")
@app.route("/home")
def home():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    return render_template("home.html", datas = data)

@app.route("/add_user", methods = ['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO users(NAME, ID, POINTS) values (?, ?, ?)", (name, id, points))
        con.commit()
        return redirect(url_for("home"))
    return render_template("add_user.html")

@app.route("/remove_user/<user>", methods = ['GET'])
def remove_user(user):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE NAME = ?", (user,))
    con.commit()
    return redirect(url_for("home"))

@app.route("/edit_user/<user>", methods = ['POST', 'GET'])
def edit_user(user):
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("UPDATE users SET NAME = ?, ID = ?, POINTS = ? WHERE NAME = ?", (name, id, points, user))
        con.commit()
        return redirect(url_for("home"))
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE NAME = ?", (user,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas = data)

@app.route("/search_user", methods = ['GET'])
def search_user():
    user = request.args.get('name', '')
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE NAME LIKE ?", ('%' + user + '%',))
    data = cur.fetchall()
    return render_template("search_user.html", datas = data)

if __name__ == "__main__":
    app.run(debug=True)
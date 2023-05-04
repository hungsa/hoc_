from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder='D:/exepython/templates')


@app.route("/")
def index():
    mydb = mysql.connector.connect(
        host="localhost",  # corrected: removed "http://" and port number
        user="root",
        password="123456",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ceo")
    data = mycursor.fetchall()

    return render_template('D:/exepython/templates/table.html', data=data)

if __name__ == '__main__':
    app.run(port=5500)  # corrected: added port number

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, redirect, url_for, render_template, flash , request

app = Flask(__name__)
db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:0946192332@127.0.0.1:5432'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True
# app.config['SQLALCHEMY_KEY'] = 'how_to_Get_KEY' 


@app.route('/')
def customer():
    return render_template("customer.html")

if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
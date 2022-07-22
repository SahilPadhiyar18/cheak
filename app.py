from telnetlib import STATUS
from this import d
from click import password_option
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os
import psycopg2

DATABASE_URL = 'postgres://qhkjicbidbltki:ff7899d0f2ef26bd2c754f6a7219d94b5c4d58de6073ad2d68d700eedb704473@ec2-44-197-128-108.compute-1.amazonaws.com:5432/d623bc8jc1utqt'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def home_page():    
    return render_template('user.html')

@app.route('/datapage', methods=['GET', 'POST']) 
def data_page():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn
    cur = conn.cursor()
    cur.execute('SELECT name FROM logindata;')
    data = cur.fetchall()
    # df = pd.DataFrame(data)
    cur.close()
    conn.close()
    dates = data 
    times = data  
    state = data  
    onbye = data  
    return render_template('datapage.html',data = dates[::-1] ,data1 = times[::-1],status = state[::-1],onby=onbye[::-1])


@app.route('/home', methods=['GET', 'POST']) 
def data():
    # dates = db.session.query(Logindata.name).all()
    # times = db.session.query(Logindata.email).all() 
    # state = db.session.query(Logindata.passsword).all() 
    # return render_template('data.html',data = dates[::-1] ,data1 = times[::-1],status = state[::-1])
    render_template('user.html')

@app.route('/switch', methods=['POST'])
def aaa():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    now = datetime.now()
    nowtime = now.strftime("%I:%M:%S %p")
    cur.execute('INSERT INTO logindata (name, email, password, addkey,logintype)'
                'VALUES (%s, %s, %s, %s, %s)',
                (nowtime, 'sahil.padhiyar18@gmail.com', 'panCh@l4060','s@hil','admin'))
    cur.execute('INSERT INTO ashok (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                'Leo Tolstoy',
                864,
                'Another great classic!')
                )
    conn.commit()
    cur.close()
    conn.close()
    return "ok"

@app.route('/swpos', methods=['GET','POST'])
def swpos():
    print("swpos")
    return "ok"


@app.route('/online', methods=['GET','POST'])
def online():
    return "data is not come"
    


if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
    # db.switch.drop()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=85)
        

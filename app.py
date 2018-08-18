from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from decouple import config
import json

app = Flask(__name__)
#configure DB
db_uri = 'mysql+pymysql://{}:{}@{}/{}'.format(config('user'), config('password'), config('host'), config('db'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode)
    description = db.Column('description', db.Unicode)
    client = db.Column('client', db.Unicode)
    priority = db.Column('priority', db.Integer)
    target_date = db.Column('target_date', db.Integer)
    product_area = db.Column('product_area', db.Integer)

    def __repr__(self):
        return '<Request %r>' % self.title

@app.route('/')
def index():
    requests = Request.query.all()
    return render_template('index.html', requests=requests)

@app.route('/add_request', methods=['POST'])
def add_request():
    form = request.form
    max_priority = Request.query.filter_by(client=form['client']).order_by(Request.priority.desc()).first().priority

    if form['priority'] > max_priority+1:
        priority = u'{}'.format(max_priority+1)
    else:
        priority = form['priority']

    update_requests = Request.query.filter(and_(Request.client==form['client'], Request.priority>=priority))
    for update_request in update_requests:
        update_request.priority += 1

    new_request = Request(
        title=form['title'],
        description=form['description'],
        client=form['client'],
        priority=priority,
        target_date=form['target_date'],
        product_area=form['product_area']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'Success':True, data: new_request})

if __name__ == '__main__':
    app.run(debug=True)

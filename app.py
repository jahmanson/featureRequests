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
    return render_template('index.html')

@app.route('/requests')
def db_requests():
    query_results = Request.query.all()
    db_requests = [
        dict(
            title=result.title,
            description=result.description,
            client=result.client,
            priority=result.priority,
            target_date=result.target_date,
            product_area=result.product_area
        ) for result in query_results
    ]
    return jsonify(db_requests=db_requests)

@app.route('/requests/new', methods=['POST'])
def add_request():
    r_json = request.json
    max_priority_item = Request.query.filter_by(client=r_json['client']).order_by(Request.priority.desc()).first()

    if max_priority_item:
        max_priority = max_priority_item.priority
    else:
        max_priority = 0

    if int(r_json['priority']) > max_priority+1:
        r_json['priority'] = unicode(max_priority+1)

    update_requests = Request.query.filter(and_(Request.client==r_json['client'], Request.priority>=r_json['priority']))
    for update_request in update_requests:
        update_request.priority += 1

    new_request = Request(
        title=r_json['title'],
        description=r_json['description'],
        client=r_json['client'],
        priority=r_json['priority'],
        target_date=r_json['target_date'],
        product_area=r_json['product_area']
    )

    db.session.add(new_request)
    db.session.commit()
    return jsonify({'success'})

if __name__ == '__main__':
    app.run(debug=True)

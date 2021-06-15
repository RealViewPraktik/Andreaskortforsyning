from flask import Flask
from flask import render_template
from flask import request
import sys

sys.path.append("..")
import DBfacade as DBF
from kafkaFlaskProducer import send_locations

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/", methods=['POST'])
def home_form_post():
    northing = request.form['northing']
    easting = request.form['easting']
    email = request.form['email']
    location = [int(easting),int(northing)]
    id = send_locations(location, email)
    return f'id: {id}, Location: {location}, email: {email}' 

@app.route("/ordre")
def order_page():
    orders = DBF.get_orders()
    str = ''
    for order in orders:
        orderID = order[0]
        location = order[1]
        image_dir = order[2]
        email = order[5]
        str += f'id: {orderID}, location: {location}, images: {image_dir}, email: {email}'
   # str += ''
    return render_template('orders.html', orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

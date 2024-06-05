from flask import Flask, render_template, request
from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS
from orders.routes import orders_bp
from orders import database_interface
from orders.utils import timeStringToInt


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your secret key'


# app.register_blueprint(orders_bp, url_prefix='/orders')




@app.route("/orders/create", methods=["POST"])
def create_order_post():
    name = request.form.get("name")
    pickUpTime = request.form.get("pickUpTime")
    items = request.form.get("items")
    phone = request.form.get("phone")
    pickUpTimeInt = timeStringToInt(pickUpTime)
    if items[0] == "'" or items[0] == '"':
        items = items[1:-1]
    if items[-1] == "'" or items[-1] == '"':
        items = items[:-1]
    print(f"{name = }, {pickUpTime = }, {pickUpTimeInt = }, {items = } {phone = }")
    return jsonify(database_interface.create_order(name, pickUpTime, pickUpTimeInt, items, phone))


@app.route("/orders/create", methods=["GET"])
def create_order_get():
    return render_template("create.html")


@app.route('/')
def index():
    return render_template('index.html', title='Home')



@app.route("/all")
def get_all_orders():
    allorders = database_interface.get_all_orders()
    return jsonify(allorders)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
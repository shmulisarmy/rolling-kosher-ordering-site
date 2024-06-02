from flask import Blueprint, request, jsonify, render_template
from . import database_interface
import json
from .utils import timeStringToInt

orders_bp = Blueprint('orders', __name__)

@orders_bp.route("/orders/<int:id>", methods=["GET"])
def get_order(id):
    return jsonify(database_interface.get_order(id))



@orders_bp.route("/create", methods=["POST"])
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

@orders_bp.route("/all", methods=["GET"])
def get_all_orders():
    allorders = database_interface.get_all_orders()
    return jsonify(allorders)
from flask import Blueprint, request, jsonify, render_template
from . import database_interface
import json
from .utils import timeStringToInt

orders_bp = Blueprint('orders', __name__)

# @orders_bp.route("/orders/<int:id>", methods=["GET"])
# def get_order(id):
#     return jsonify(database_interface.get_order(id))




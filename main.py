from flask import Flask, render_template, request
from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS
from orders.routes import orders_bp


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your secret key'


app.register_blueprint(orders_bp, url_prefix='/orders')


@app.route('/')
def index():
    return render_template('index.html', title='Home')


# @app.after_request
# def add_header(response):
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

#run command: uvicorn main:app --reload

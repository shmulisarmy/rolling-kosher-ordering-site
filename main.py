from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/items", methods=["POST"])
def hello():
    items = request.get_json()
    print(f"got from user: {items}")
    return {"message": "this items were added to the cart"}


if __name__ == '__main__':
    app.run(debug=True)

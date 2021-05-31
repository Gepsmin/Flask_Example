from flask import Flask, request
import pymongo
import helper_functions
import requests


app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://base_user:base_user_password@cluster0.dbcb9.mongodb.net/first")
db = client.first
col = db.col


@app.route('/add_user/<user_id>/<user_name>/<user_password>', methods=["POST"])
def add_user(user_id, user_name, user_password):
    if request.method == "POST":
        helper_functions.create_user(user_id, user_name, user_password, col)
    result = "id:" + user_id + " name:" + user_name + " password:" + user_password
    return result


@app.route("/get_user/<user_name>/<user_password>", methods=["GET"])
def get_user(user_name, user_password):
    if request.method == "GET":
        x = helper_functions.get_user(user_name, user_password, col)
        return x


@app.route('/', methods=["GET"])
def index():
    header = {
        "Accept": 'application/json'
    }
    x = requests.post('http://127.0.0.1:5000/add_user/352/Ogrenci/sifre')
    y = requests.get('https://official-joke-api.appspot.com/random_joke')
    z = requests.get('https://covid-api.mmediagroup.fr/v1/cases?country=Turkey')
    return y.json()


if __name__ == "__main__":
    app.run(debug=True)

from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, Field, SubmitField
from flask import Flask, render_template
from wtforms.widgets import TextInput
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from typing import List
import requests


#### Initialize App
app = Flask(__name__)
app.config['SECRET_KEY'] = "laiweuhf"
Bootstrap5(app)


#### Create db
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

load_dotenv()

GH_TOKEN = os.environ["GITHUB_TOKEN"]
GH_USERNAME = os.environ["GITHUB_USERNAME"]


# def get_events():
#     headers = {
#         "accept": "application/vnd.github+json",
#         "authorization": f"Bearer {GH_TOKEN}",
#         "X-GitHub-Api-Version": "2022-11-28"
#     }
#
#     api_url = "https://api.github.com/"
#
#     user_events = f"{api_url}users/{GH_USERNAME}/events"
#
#     response = requests.get(url=user_events, headers=headers)
#     response.raise_for_status()
#     events = response.json()
#
#     return events


@app.route('/')
def home():
    headers = {
        "accept": "application/vnd.github+json",
        "authorization": f"Bearer {GH_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    api_url = "https://api.github.com/"

    user_events = f"{api_url}users/{GH_USERNAME}/events"

    response = requests.get(url=user_events, headers=headers)
    response.raise_for_status()
    events = response.json()








if __name__ == '__main__':
    app.run(debug=True, port=5010)
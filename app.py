'''routes for pet adoption agency'''

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "asdfhl45lhasdf"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    '''homepage'''
    return redirect('/pets/list')

@app.route('/pets/list')
def show_pets():
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/pets/new', methods=["GET"])
def new_pet_form():
    '''Display new pet form'''
    return render_template('pets/new.html')

@app.route('/pets/new', methods=["POST"])
def create_pet():
    '''Create new pet'''
    name = request.form(['name'])
    species = request.form(['species'])
    
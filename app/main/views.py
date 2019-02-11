from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required

# Views 
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = "Welcome to One Time Pitch"
    return render_template('index.html', title = title)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):


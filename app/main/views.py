from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm
from .. import db

@main.route('/')
def index():
   
    return render_template('index.html')

@main.route('/pitches/new_pitch', methods=['GET','POST'])
def new_pitch():
    form = ReviewForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
    return render_template('new_pitch.html', review_form=form)

@main.route('/pitches/marketing_pitches')
def marketing_pitches():
    return render_template('marketing.html')

@main.route('/pitches/promotional_pitches')
def promotion_pitches():
    return render_template('promotion.html')

@main.route('/pitches/scholarship_pitches')
def scholar_pitches():
    return render_template('scholar.html')


    

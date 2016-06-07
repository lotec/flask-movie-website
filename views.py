from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Features

app = Flask(__name__)

engine = create_engine('sqlite:///app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/index/')
def showIndex():
    all_titles = session.query(Movie).all()
    all_filenames = session.query(Features).all()

    return render_template('body.html', getall=zip(all_titles, all_filenames))


@app.route('/index/<int:movie_id>/')
def showMoviePage(movie_id):
    movie_title = session.query(Movie).filter_by(id=movie_id).one()
    all_features = session.query(Features).filter_by(id=movie_id).one()

    return render_template('moviepage.html', movie_title=movie_title, all_features=all_features, movie_id=movie_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
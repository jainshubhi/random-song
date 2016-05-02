import os
import spotify
import random

from flask import Flask
from flask import render_template
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy


################################### CONFIG #####################################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Emotion
################################### ROUTES #####################################
@app.route('/random')
def random_song():
    song = random.choice(spotify.get_random_songs())
    return render_template('random.html', song=song)

@app.route('/')
def visualize():
    return 'Visualize Spotify Emotions'

@app.route('/<emotion>')
def emotion_song(emotion):
    return "Hello {}!".format(emotion)

#################################### RUN #######################################
if __name__ == '__main__':
    app.run()

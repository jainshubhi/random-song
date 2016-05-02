import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


################################### CONFIG #####################################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Emotion
################################### ROUTES #####################################
@app.route('/random')
def random():
    return "Hello World!"


@app.route('/<emotion>')
def emotion(emotion):
    return "Hello {}!".format(emotion)

#################################### RUN #######################################
if __name__ == '__main__':
    app.run()

import os
import requests

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy


################################### CONFIG #####################################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Emotion
################################### ROUTES #####################################
@app.route('/random')
def random():
    r = requests.get('http://randomword.setgetgo.com/get.php')
    return render_template('random.html', random_word=r.text)


@app.route('/<emotion>')
def emotion(emotion):
    return "Hello {}!".format(emotion)

#################################### RUN #######################################
if __name__ == '__main__':
    app.run()

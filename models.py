from app import db
from sqlalchemy.dialects.postgresql import JSON


class Emotion(db.Model):
    __tablename__ = 'emotions'

    uri = db.Column(db.String(), primary_key=True)
    audio_features = db.Column(JSON)
    anger = db.Column(db.Integer)
    contempt = db.Column(db.Integer)
    disgust = db.Column(db.Integer)
    fear = db.Column(db.Integer)
    happiness = db.Column(db.Integer)
    neutral = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    surprise = db.Column(db.Integer)
    none = db.Column(db.Integer)

    def __init__(self, uri, audio_features):
        self.url = uri
        self.result_all = audio_features
        self.anger = 0
        self.contempt = 0
        self.disgust = 0
        self.fear = 0
        self.happiness = 0
        self.neutral = 0
        self.sadness = 0
        self.surprise = 0
        self.none = 0

    def __repr__(self):
        return '<uri %r>' % self.uri

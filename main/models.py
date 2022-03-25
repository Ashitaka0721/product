from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone
import pytz
from sqlalchemy import Unicode

"""
class Entry(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   jcode = db.Column(db.String)
   temp = db.Column(db.Float)
   date = db.Column(db.DateTime, default=datetime.now()) 

   def __repr__(self):
       return "<Entry id={} jcode={!r} temp={!r} date={}>".format(self.id, self.jcode, self.temp, self.date)

"""
class Entry(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    ate = db.Column(Unicode(255))
    amount = db.Column(Unicode(255))
    ate_at = db.Column(db.DateTime, nullable=False,
                    default=datetime.now(pytz.timezone('Asia/Tokyo')))
    def __repr__(self):
        return '<User %r>' % self.username

def init():
   db.create_all()


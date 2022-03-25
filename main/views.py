import flask 
from main import app, db  #インポート対象にdbを追加
from main.models import Entry

@app.route('/')
def show_entries():
   entries = Entry.query.all()
   return flask.render_template('entries.html', entries=entries)

# DBにデータを追加するadd_entry関数を定義
@app.route('/add', methods=['POST'])
def add_entry():
   entry = Entry(ate = flask.request.form['ate'],amount = flask.request.form['amount'])
   db.session.add(entry)
   db.session.commit()
   return flask.redirect(flask.url_for('show_entries'))
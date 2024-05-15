import pathlib
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'decidedtotryflaskapp'


def get_db_connection():
   """Connect to database."""
   db_file_path = pathlib.Path(__file__).parent.resolve()
   db_file = f"{db_file_path}\\filmflix.db"
   print(f"{db_file=}")
   conn = sqlite3.connect(db_file)
   conn.row_factory = sqlite3.Row
   return conn


#fetching, redirecting and displaying only one film
def get_film(film_id):
   conn = get_db_connection()
   film = conn.execute('SELECT * FROM tblFilms WHERE filmID = ?', (film_id,)).fetchone()
   conn.close()
   if film is None:
      abort(404)
   return film

@app.route("/<int:film_id>")
def film(film_id):
  film  = get_film(film_id)
  return render_template('film.html', film=film)


#directing to index page
@app.route("/")
def index():
  conn  = get_db_connection()
  films = conn.execute('SELECT * FROM tblFilms').fetchall()
  conn.close()
  return render_template('index.html', films=films)




#adding and redirecting to create page
@app.route("/create", methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
     title = request.form['title']
     yearReleased = request.form['yearReleased']
     rating = request.form['rating']
     duration = request.form['duration']
     genre = request.form['genre']

     if not title:
        flash('Title is requiered')
     else:
        conn = get_db_connection()
        conn.execute('INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)', (title, yearReleased, rating, duration, genre))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
     
  return render_template('create.html')




#updating and redirecting to update page
@app.route("/<int:id>/update", methods=('GET', 'POST'))
def update(id):
  film = get_film(id)

  if request.method == 'POST':
     title = request.form['title']
     yearReleased = request.form['yearReleased']
     rating = request.form['rating']
     duration = request.form['duration']
     genre = request.form['genre']

     if not title:
        flash('Title is required')
     else:
        conn = get_db_connection()
        conn.execute('UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?', (title, yearReleased, rating, duration, genre, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
     
  return render_template('update.html', film=film)





if __name__ == "__main__":
    app.run(debug=True)
"""Main script to run my webservice."""

import pathlib
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "decidedtotryflaskapp"


def get_db_connection():
    """Connect to database."""
    db_file_path = pathlib.Path(__file__).parent.resolve() / "filmflix.db"
    conn = sqlite3.connect(db_file_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_film(film_id: str):
    """Fetch and redirect and display single data."""
    conn = get_db_connection()
    current_film = conn.execute(
        "SELECT * FROM tblFilms WHERE filmID = ?", (film_id,)
    ).fetchone()
    conn.close()
    if current_film is None:
        abort(404)
    return current_film


@app.route("/<int:film_id>")
def film(film_id: str):
    """Get specific film."""
    current_film = get_film(film_id)
    return render_template("film.html", film=current_film)


@app.route("/")
def index():
    """Route to index page."""
    conn = get_db_connection()
    films = conn.execute("SELECT * FROM tblFilms").fetchall()
    conn.close()
    return render_template("index.html", films=films)


@app.route("/create", methods=("GET", "POST"))
def create():
    """Add and redirect to create page."""
    if request.method == "POST":
        title = request.form["title"]
        yearReleased = request.form["yearReleased"]
        rating = request.form["rating"]
        duration = request.form["duration"]
        genre = request.form["genre"]

        if not title:
            flash("Title is requiered")
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
                (title, yearReleased, rating, duration, genre),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("create.html")



@app.route("/<int:id>/update", methods=("GET", "POST"))
def update(id):
    """Update and redirect to update page"""
    film = get_film(id)

    if request.method == "POST":
        title = request.form["title"]
        yearReleased = request.form["yearReleased"]
        rating = request.form["rating"]
        duration = request.form["duration"]
        genre = request.form["genre"]

        if not title:
            flash("Title is required")
        else:
            conn = get_db_connection()
            conn.execute(
                "UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?",
                (title, yearReleased, rating, duration, genre, id),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("update.html", film=film)


@app.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    """Delete single data."""
    current_film = get_film(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tblFilms WHERE filmID = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(current_film['title']))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

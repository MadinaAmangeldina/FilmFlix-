from connect import *

def insertFilm():
  #create an empty list
  films = []

  #obtain values from the user
  title = input("Enter Film Title: ")
  yearReleased = input("Enter year released: ")
  rating = input("Enter film rating: ")
  duration = input("Enter film duration: ")
  genre = input("Enter Genre: ")

  #append data to the list "songs"
  films.append(title)
  films.append(yearReleased)
  films.append(rating)
  films.append(duration)
  films.append(genre)
  # print(songs)
  # songs = songs + [title, artist, genre]
  # print(songs)

  try:
    cursor.execute(" INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", films)
    conn.commit() # .commit() makes the change permenent
    print(f"{title} added to the films table")

  except sql.OperationalError as e:
    conn.rollback()
    print(f"Record not added: {e}")

if __name__ == "__main__":
  insertFilm()